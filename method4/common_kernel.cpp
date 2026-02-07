#include "common_kernel.h"

#include <dlfcn.h>
#include <filesystem>
#include <system_error>
#include <stdexcept>
#include <string>

#if defined(__APPLE__)
#include <mach-o/dyld.h>
#elif defined(__linux__)
#include <limits.h>
#include <unistd.h>
#endif

namespace {
std::filesystem::path get_executable_path() {
#if defined(__APPLE__)
  uint32_t size = 0;
  _NSGetExecutablePath(nullptr, &size);
  std::string buf(size, '\0');
  if (_NSGetExecutablePath(buf.data(), &size) != 0) {
    throw std::runtime_error("Failed to get executable path");
  }
  return std::filesystem::weakly_canonical(std::filesystem::path(buf.c_str()));
#elif defined(__linux__)
  char buf[PATH_MAX];
  ssize_t len = ::readlink("/proc/self/exe", buf, sizeof(buf) - 1);
  if (len <= 0) {
    throw std::runtime_error("Failed to read /proc/self/exe");
  }
  buf[len] = '\0';
  return std::filesystem::weakly_canonical(std::filesystem::path(buf));
#else
  return {};
#endif
}

std::filesystem::path get_this_shared_object_path() {
  Dl_info info;
  if (dladdr(reinterpret_cast<const void*>(&get_this_shared_object_path), &info) != 0 &&
      info.dli_fname) {
    std::error_code ec;
    return std::filesystem::weakly_canonical(std::filesystem::path(info.dli_fname), ec);
  }
  return {};
}

std::filesystem::path resolve_common_kernel_path() {
  std::error_code ec;

  // 1) If we're in a shared library (e.g., a Python extension), prefer locating
  // `libcommon` next to that library (repo layout puts both under `common/`).
  const auto self = get_this_shared_object_path();
  if (!self.empty()) {
    const auto dir = self.parent_path();
    // Prefer lib/ subdirectory (avoids Python import conflict with libcommon.py).
    for (const auto& search_dir : {dir / "lib", dir}) {
      const auto dylib = search_dir / "libcommon.dylib";
      const auto so = search_dir / "libcommon.so";
      if (std::filesystem::exists(dylib, ec)) {
        return dylib;
      }
      if (std::filesystem::exists(so, ec)) {
        return so;
      }
    }
  }

  // Prefer locating relative to the executable, so running from method4/build works.
  const auto exe = get_executable_path();
  if (!exe.empty()) {
    const auto root = exe.parent_path() / ".." / "..";
    for (const auto& base : {root / "common" / "lib", root / "common"}) {
      const auto so = base / "libcommon.so";
      const auto dylib = base / "libcommon.dylib";
      if (std::filesystem::exists(dylib, ec)) {
        return dylib;
      }
      if (std::filesystem::exists(so, ec)) {
        return so;
      }
    }
  }

  // Fallback to working directory relative paths.
  for (const auto& base : {std::filesystem::path("common") / "lib",
                            std::filesystem::path("common")}) {
    const auto so = base / "libcommon.so";
    const auto dylib = base / "libcommon.dylib";
    if (std::filesystem::exists(dylib, ec)) {
      return dylib;
    }
    if (std::filesystem::exists(so, ec)) {
      return so;
    }
  }

  // Last resort: return the canonical target (error message will include it).
  return std::filesystem::path("common") / "lib" / "libcommon.so";
}
}  // namespace

CommonApi load_common_api() {
  const std::string so_path = resolve_common_kernel_path().string();

  void* handle = dlopen(so_path.c_str(), RTLD_LAZY);
  if (!handle) {
    throw std::runtime_error("Failed to load libcommon: " + so_path);
  }

  auto add_fn = reinterpret_cast<LaunchAddKernelFn>(dlsym(handle, "add"));
  if (!add_fn) {
    throw std::runtime_error("Failed to find add");
  }

  auto alloc_fn = reinterpret_cast<AllocateBufFn>(dlsym(handle, "allocate_buf"));
  if (!alloc_fn) {
    throw std::runtime_error("Failed to find allocate_buf");
  }

  auto free_fn = reinterpret_cast<FreeBufFn>(dlsym(handle, "free_buf"));
  if (!free_fn) {
    throw std::runtime_error("Failed to find free_buf");
  }

  CommonApi api;
  api.handle = handle;
  api.add = add_fn;
  api.allocate_buf = alloc_fn;
  api.free_buf = free_fn;
  return api;
}

