#include <chrono>
#include <iostream>
#include <string>
#include <tuple>
#include <array>

#include "common_kernel.h"
#include "op_add.h"
#include "op_reshape.h"

namespace {
constexpr int kRank = 8;

std::string parse_device(int argc, char** argv) {
  // Simple flag parser: --device cpu|cuda
  std::string device = "cpu";
  for (int i = 1; i + 1 < argc; ++i) {
    if (std::string(argv[i]) == "--device") {
      device = argv[i + 1];
    }
  }
  return device;
}

std::array<int64_t, kRank> contiguous_stride(const std::array<int64_t, kRank>& shape) {
  std::array<int64_t, kRank> stride{};
  for (int i = 0; i < kRank; ++i) {
    stride[static_cast<size_t>(i)] = 1;
  }
  for (int64_t i = static_cast<int64_t>(kRank) - 2; i >= 0; --i) {
    stride[static_cast<size_t>(i)] =
        stride[static_cast<size_t>(i + 1)] * shape[static_cast<size_t>(i + 1)];
  }
  return stride;
}

TensorView<kRank> emulate_chain(const TensorView<kRank>& in, const CommonApi& api) {
  const std::array<int64_t, kRank> shape_a = {19, 17, 13, 11, 7, 5, 3, 2};
  const std::array<int64_t, kRank> shape_b = {2, 3, 5, 7, 11, 13, 17, 19};

  auto tmp1 = add<kRank>(in, 1.0f, api);
  auto v1 = reshape<kRank, kRank>(tmp1, shape_a);
  auto tmp2 = add<kRank>(v1, -1.0f, api);
  api.free_buf(tmp1.ptr);

  auto v2 = reshape<kRank, kRank>(tmp2, shape_b);
  auto tmp3 = add<kRank>(v2, 0.0f, api);
  api.free_buf(tmp2.ptr);

  return tmp3;
}
}  // namespace

int main(int argc, char** argv) {
  const int64_t loops = 100;

  // Device selection is controlled by which `libcommon` was built/loaded.
  // Keep `--device` for CLI compatibility.
  (void)parse_device(argc, argv);

  const std::array<int64_t, kRank> shape_b = {2, 3, 5, 7, 11, 13, 17, 19};
  const auto stride_b = contiguous_stride(shape_b);

  auto api = load_common_api();
  int64_t numel_b = 1;
  for (auto d : shape_b) {
    numel_b *= d;
  }
  TensorView<kRank> view;
  view.ptr = api.allocate_buf(numel_b * static_cast<int64_t>(sizeof(float)));
  view.shape = shape_b;
  view.stride = stride_b;

  auto start = std::chrono::high_resolution_clock::now();
  auto out = view;
  for (int64_t i = 0; i < loops; ++i) {
    const auto old_ptr = out.ptr;
    out = emulate_chain(out, api);
    api.free_buf(old_ptr);
  }
  auto end = std::chrono::high_resolution_clock::now();
  auto duration = std::chrono::duration_cast<std::chrono::duration<double>>(end - start);
  // Free final result after timing.
  api.free_buf(out.ptr);
  std::cout << "method4_custom_seconds=" << duration.count() << std::endl;
  return 0;
}
