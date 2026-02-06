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

std::filesystem::path resolve_common_kernel_path() {
  std::error_code ec;

  // Prefer locating relative to the executable, so running from method4/build works.
  const auto exe = get_executable_path();
  if (!exe.empty()) {
    const auto root = exe.parent_path() / ".." / "..";
    const auto so = root / "common" / "libcommon.so";
    const auto dylib = root / "common" / "libcommon.dylib";
    if (std::filesystem::exists(so, ec)) {
      return so;
    }
    if (std::filesystem::exists(dylib, ec)) {
      return dylib;
    }
  }

  // Fallback to working directory relative paths.
  const auto so = std::filesystem::path("common") / "libcommon.so";
  const auto dylib = std::filesystem::path("common") / "libcommon.dylib";
  if (std::filesystem::exists(so, ec)) {
    return so;
  }
  if (std::filesystem::exists(dylib, ec)) {
    return dylib;
  }

  // Last resort: return the canonical target (error message will include it).
  return so;
}
}  // namespace

LaunchAddKernelFn load_common_kernel() {
  const std::string so_path = resolve_common_kernel_path().string();

  void* handle = dlopen(so_path.c_str(), RTLD_LAZY);
  if (!handle) {
    throw std::runtime_error("Failed to load common.so: " + so_path);
  }

  auto fn = reinterpret_cast<LaunchAddKernelFn>(
      dlsym(handle, "add1d"));
  if (!fn) {
    throw std::runtime_error("Failed to find add1d");
  }
  return fn;
}

