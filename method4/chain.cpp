#include "chain.h"

#include <array>
#include <cstddef>
#include <cstdint>

#include "common_kernel.h"
#include "op_add.h"
#include "op_reshape.h"

namespace {

std::array<int64_t, 8> contiguous_stride(const std::array<int64_t, 8>& shape) {
  std::array<int64_t, 8> stride{};
  for (int i = 0; i < 8; ++i) {
    stride[static_cast<size_t>(i)] = 1;
  }
  for (int64_t i = 6; i >= 0; --i) {
    stride[static_cast<size_t>(i)] =
        stride[static_cast<size_t>(i + 1)] * shape[static_cast<size_t>(i + 1)];
  }
  return stride;
}

const std::array<int64_t, 8> shape_b = {2, 3, 5, 7, 11, 13, 17, 19};
const auto stride_b = contiguous_stride(shape_b);

TensorView<8> emulate_chain(const TensorView<8>& in, const CommonApi& api) {
  const std::array<int64_t, 8> shape_a = {19, 17, 13, 11, 7, 5, 3, 2};

  auto v1 = reshape<8, 8>(in, shape_a);
  auto tmp1 = add<8>(v1, 0.0f, api);

  auto v2 = reshape<8, 8>(tmp1, shape_b);

  return {v2.ptr, v2.shape, v2.stride};
}
}  // namespace

uint64_t method4_create_input() {
  auto api = load_common_api();

  int64_t numel_b = 1;
  for (auto d : shape_b) {
    numel_b *= d;
  }

  return api.allocate_buf(numel_b * static_cast<int64_t>(sizeof(float)));
}

uint64_t method4_custom_chain(uint64_t in_ptr) {
  auto api = load_common_api();

  TensorView<8> view;
  view.ptr = in_ptr;
  view.shape = shape_b;
  view.stride = stride_b;

  auto out = view;
  for (int64_t i = 0; i < 100; ++i) {
    const auto old_ptr = out.ptr;
    out = emulate_chain(out, api);
    api.free_buf(old_ptr);
  }

  return out.ptr;
}

void method4_free_buf(uint64_t ptr) {
  auto api = load_common_api();
  api.free_buf(ptr);
}
