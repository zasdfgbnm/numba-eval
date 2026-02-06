#include "op_reshape.h"

#include <functional>
#include <numeric>
#include <stdexcept>

namespace {
int64_t numel(const std::vector<int64_t>& shape) {
  return std::accumulate(
      shape.begin(), shape.end(), int64_t{1}, std::multiplies<int64_t>());
}

std::vector<int64_t> infer_size(int64_t total, const std::vector<int64_t>& shape) {
  std::vector<int64_t> inferred = shape;
  int64_t known = 1;
  int64_t unknown = -1;
  for (size_t i = 0; i < shape.size(); ++i) {
    if (shape[i] == -1) {
      if (unknown != -1) {
        throw std::runtime_error("Only one inferred dimension allowed");
      }
      unknown = static_cast<int64_t>(i);
    } else {
      if (shape[i] <= 0) {
        throw std::runtime_error("Invalid shape");
      }
      known *= shape[i];
    }
  }

  if (unknown != -1) {
    if (total % known != 0) {
      throw std::runtime_error("Inferred dimension mismatch");
    }
    inferred[unknown] = total / known;
  }

  if (numel(inferred) != total) {
    throw std::runtime_error("Reshape numel mismatch");
  }
  return inferred;
}

std::vector<int64_t> compute_view_stride(const std::vector<int64_t>& shape,
                                         const std::vector<int64_t>& stride,
                                         const std::vector<int64_t>& new_shape) {
  if (numel(shape) != numel(new_shape)) {
    throw std::runtime_error("Reshape numel mismatch");
  }
  if (shape.empty()) {
    return {};
  }

  std::vector<int64_t> view_stride(new_shape.size(), 0);
  int64_t view_dim = static_cast<int64_t>(new_shape.size()) - 1;
  int64_t chunk_base_stride = stride.back();
  int64_t tensor_numel = 1;
  int64_t view_numel = 1;

  for (int64_t tensor_dim = static_cast<int64_t>(shape.size()) - 1; tensor_dim >= 0;
       --tensor_dim) {
    tensor_numel *= shape[tensor_dim];
    bool at_chunk_end = tensor_dim == 0;
    if (!at_chunk_end) {
      auto expected = shape[tensor_dim] * stride[tensor_dim];
      if (shape[tensor_dim - 1] != 1 && stride[tensor_dim - 1] != expected) {
        at_chunk_end = true;
      }
    }

    if (at_chunk_end) {
      while (view_dim >= 0 && (view_numel < tensor_numel || new_shape[view_dim] == 1)) {
        view_stride[view_dim] = chunk_base_stride * view_numel;
        view_numel *= new_shape[view_dim];
        --view_dim;
      }
      if (view_numel != tensor_numel) {
        throw std::runtime_error("View not compatible");
      }
      if (tensor_dim > 0) {
        chunk_base_stride = stride[tensor_dim - 1];
        tensor_numel = 1;
        view_numel = 1;
      }
    }
  }

  while (view_dim >= 0) {
    if (new_shape[view_dim] != 1) {
      throw std::runtime_error("View not compatible");
    }
    view_stride[view_dim] = chunk_base_stride * view_numel;
    view_numel *= new_shape[view_dim];
    --view_dim;
  }

  return view_stride;
}
}  // namespace

std::pair<std::vector<int64_t>, std::vector<int64_t>> reshape_with_checks(
    const std::vector<int64_t>& shape,
    const std::vector<int64_t>& stride,
    const std::vector<int64_t>& target_shape) {
  auto inferred = infer_size(numel(shape), target_shape);
  auto target_stride = compute_view_stride(shape, stride, inferred);
  return {inferred, target_stride};
}

