#include "op_add.h"

#include <array>
#include <cstdint>
#include <functional>
#include <numeric>
#include <stdexcept>

namespace {
template <int Rank>
int64_t numel(const std::array<int64_t, Rank>& shape) {
  int64_t out = 1;
  for (int i = 0; i < Rank; ++i) {
    out *= shape[static_cast<size_t>(i)];
  }
  return out;
}

template <int Rank>
void check_contiguous(const std::array<int64_t, Rank>& shape,
                      const std::array<int64_t, Rank>& stride) {
  int64_t expected = 1;
  for (int64_t i = static_cast<int64_t>(Rank); i-- > 0;) {
    const auto idx = static_cast<size_t>(i);
    if (stride[idx] != expected) {
      throw std::runtime_error("non-contiguous view");
    }
    expected *= shape[idx];
  }
}
}  // namespace

template <int Rank>
TensorView<Rank> add(const TensorView<Rank>& in, float value, const CommonApi& api) {
  check_contiguous<Rank>(in.shape, in.stride);
  const int64_t total = numel<Rank>(in.shape);
  const uint64_t out_ptr = api.allocate_buf(total * static_cast<int64_t>(sizeof(float)));
  api.add(reinterpret_cast<const float*>(in.ptr),
          reinterpret_cast<float*>(out_ptr),
          total,
          value);
  TensorView<Rank> out;
  out.ptr = out_ptr;
  out.shape = in.shape;
  out.stride = in.stride;
  return out;
}

template TensorView<8> add<8>(const TensorView<8>&, float, const CommonApi&);

