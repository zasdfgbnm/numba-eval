#include "chain.h"

#include <dlfcn.h>
#include <filesystem>
#include <stdexcept>
#include <string>
#include <torch/torch.h>
#include <vector>

namespace {

using NormalizeKernelFn = void (*)(const float*, float*, int64_t, int64_t, int64_t);

NormalizeKernelFn load_normalize_fn() {
  // Try to find libcommon.so relative to this shared object.
  Dl_info info;
  std::filesystem::path so_dir;
  if (dladdr(reinterpret_cast<const void*>(&load_normalize_fn), &info) != 0 &&
      info.dli_fname) {
    std::error_code ec;
    so_dir = std::filesystem::weakly_canonical(
                 std::filesystem::path(info.dli_fname), ec)
                 .parent_path();
  }

  std::vector<std::string> candidates;
  if (!so_dir.empty()) {
    candidates.push_back((so_dir / "lib" / "libcommon.so").string());
    candidates.push_back((so_dir / "lib" / "libcommon.dylib").string());
    candidates.push_back((so_dir / "libcommon.so").string());
    candidates.push_back((so_dir / "libcommon.dylib").string());
  }
  candidates.push_back("common/lib/libcommon.so");
  candidates.push_back("common/lib/libcommon.dylib");

  void* handle = nullptr;
  for (const auto& path : candidates) {
    handle = dlopen(path.c_str(), RTLD_LAZY);
    if (handle) break;
  }
  if (!handle) {
    throw std::runtime_error("Failed to load libcommon for normalize");
  }

  auto fn = reinterpret_cast<NormalizeKernelFn>(dlsym(handle, "normalize"));
  if (!fn) {
    throw std::runtime_error("Failed to find normalize in libcommon");
  }
  return fn;
}

}  // namespace

void method2_libtorch_chain(const at::Tensor& tensor) {
  const std::vector<int64_t> shape_a = {19, 17, 13, 11, 7, 5, 3, 2};
  const std::vector<int64_t> shape_b = {2, 3, 5, 7, 11, 13, 17, 19};

  static auto normalize_fn = load_normalize_fn();

  // Match benchmark intent: focus on dispatch/overhead, not autograd.
  torch::NoGradGuard no_grad;

  auto out = tensor;
  for (int64_t i = 0; i < 100; ++i) {
    out = out.reshape(shape_a);

    // Allocate output tensor via LibTorch, call our single-kernel normalize.
    auto result = at::empty_like(out);
    int64_t numel = out.numel();
    int64_t dim = i % 4;
    int64_t reduce_dim_size = shape_a[static_cast<size_t>(dim)];
    int64_t dim_stride = 1;
    for (int64_t d = dim + 1; d < 8; ++d) {
      dim_stride *= shape_a[static_cast<size_t>(d)];
    }
    normalize_fn(out.data_ptr<float>(), result.data_ptr<float>(),
                 numel, reduce_dim_size, dim_stride);
    out = result;

    out = out.reshape(shape_b);
  }
}
