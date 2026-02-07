#include "op_reshape.h"

#include <array>
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

template <int OutRank>
std::array<int64_t, OutRank> infer_size(int64_t total,
                                        const std::array<int64_t, OutRank>& shape) {
  std::array<int64_t, OutRank> inferred = shape;
  int64_t known = 1;
  int64_t unknown = -1;
  for (int i = 0; i < OutRank; ++i) {
    if (shape[static_cast<size_t>(i)] == -1) {
      if (unknown != -1) {
        throw std::runtime_error("Only one inferred dimension allowed");
      }
      unknown = static_cast<int64_t>(i);
    } else {
      if (shape[static_cast<size_t>(i)] <= 0) {
        throw std::runtime_error("Invalid shape");
      }
      known *= shape[static_cast<size_t>(i)];
    }
  }

  if (unknown != -1) {
    if (total % known != 0) {
      throw std::runtime_error("Inferred dimension mismatch");
    }
    inferred[static_cast<size_t>(unknown)] = total / known;
  }

  if (numel<OutRank>(inferred) != total) {
    throw std::runtime_error("Reshape numel mismatch");
  }
  return inferred;
}

template <int InRank, int OutRank>
std::array<int64_t, OutRank> compute_view_stride(
    const std::array<int64_t, InRank>& shape,
    const std::array<int64_t, InRank>& stride,
    const std::array<int64_t, OutRank>& new_shape) {
  if (numel<InRank>(shape) != numel<OutRank>(new_shape)) {
    throw std::runtime_error("Reshape numel mismatch");
  }
  std::array<int64_t, OutRank> view_stride{};
  int64_t view_dim = static_cast<int64_t>(OutRank) - 1;
  int64_t chunk_base_stride = stride[static_cast<size_t>(InRank - 1)];
  int64_t tensor_numel = 1;
  int64_t view_numel = 1;

  for (int64_t tensor_dim = static_cast<int64_t>(InRank); tensor_dim-- > 0;) {
    tensor_numel *= shape[static_cast<size_t>(tensor_dim)];
    bool at_chunk_end = tensor_dim == 0;
    if (!at_chunk_end) {
      const auto td = static_cast<size_t>(tensor_dim);
      const auto prev = static_cast<size_t>(tensor_dim - 1);
      auto expected = shape[td] * stride[td];
      if (shape[prev] != 1 && stride[prev] != expected) {
        at_chunk_end = true;
      }
    }

    if (at_chunk_end) {
      while (view_dim >= 0 &&
             (view_numel < tensor_numel ||
              new_shape[static_cast<size_t>(view_dim)] == 1)) {
        view_stride[static_cast<size_t>(view_dim)] = chunk_base_stride * view_numel;
        view_numel *= new_shape[static_cast<size_t>(view_dim)];
        --view_dim;
      }
      if (view_numel != tensor_numel) {
        throw std::runtime_error("View not compatible");
      }
      if (tensor_dim > 0) {
        chunk_base_stride = stride[static_cast<size_t>(tensor_dim - 1)];
        tensor_numel = 1;
        view_numel = 1;
      }
    }
  }

  while (view_dim >= 0) {
    if (new_shape[static_cast<size_t>(view_dim)] != 1) {
      throw std::runtime_error("View not compatible");
    }
    view_stride[static_cast<size_t>(view_dim)] = chunk_base_stride * view_numel;
    view_numel *= new_shape[static_cast<size_t>(view_dim)];
    --view_dim;
  }

  return view_stride;
}
}  // namespace

template <int InRank, int OutRank>
TensorView<OutRank> reshape(const TensorView<InRank>& in,
                            const std::array<int64_t, OutRank>& target_shape) {
  TensorView<OutRank> out;
  out.ptr = in.ptr;
  out.shape = infer_size<OutRank>(numel<InRank>(in.shape), target_shape);
  out.stride = compute_view_stride<InRank, OutRank>(in.shape, in.stride, out.shape);
  return out;
}

template TensorView<8> reshape<8, 8>(const TensorView<8>&,
                                     const std::array<int64_t, 8>&);

