#include "op_add.h"

#include <cstdint>
#include <functional>
#include <numeric>
#include <stdexcept>

namespace {
int64_t numel(const std::vector<int64_t>& shape) {
  return std::accumulate(
      shape.begin(), shape.end(), int64_t{1}, std::multiplies<int64_t>());
}

void check_contiguous(const std::vector<int64_t>& shape, const std::vector<int64_t>& stride) {
  if (shape.size() != stride.size()) {
    throw std::runtime_error("shape/stride rank mismatch");
  }
  int64_t expected = 1;
  for (int64_t i = static_cast<int64_t>(shape.size()) - 1; i >= 0; --i) {
    if (stride[static_cast<size_t>(i)] != expected) {
      throw std::runtime_error("non-contiguous view");
    }
    expected *= shape[static_cast<size_t>(i)];
  }
}
}  // namespace

TensorView add(const TensorView& in, float value, const CommonApi& api) {
  check_contiguous(in.shape, in.stride);
  const int64_t total = numel(in.shape);
  const uint64_t out_ptr = api.allocate_buf(total * static_cast<int64_t>(sizeof(float)));
  api.add(reinterpret_cast<const float*>(in.ptr),
          reinterpret_cast<float*>(out_ptr),
          total,
          value);
  TensorView out;
  out.ptr = out_ptr;
  out.shape = in.shape;
  out.stride = in.stride;
  return out;
}

