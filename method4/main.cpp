#include <chrono>
#include <iostream>
#include <numeric>
#include <torch/torch.h>

namespace {
int64_t numel(const std::vector<int64_t>& shape) {
  return std::accumulate(shape.begin(), shape.end(), int64_t{1}, std::multiplies<int64_t>());
}

std::vector<int64_t> contiguous_stride(const std::vector<int64_t>& shape) {
  std::vector<int64_t> stride(shape.size(), 1);
  for (int64_t i = static_cast<int64_t>(shape.size()) - 2; i >= 0; --i) {
    stride[i] = stride[i + 1] * shape[i + 1];
  }
  return stride;
}

bool is_contiguous(const std::vector<int64_t>& shape, const std::vector<int64_t>& stride) {
  return stride == contiguous_stride(shape);
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

bool can_view(const std::vector<int64_t>& shape,
              const std::vector<int64_t>& stride,
              const std::vector<int64_t>& new_shape) {
  if (numel(shape) != numel(new_shape)) {
    return false;
  }
  if (is_contiguous(shape, stride)) {
    return true;
  }
  std::vector<int64_t> view_dims;
  std::vector<int64_t> view_strides;
  for (size_t i = 0; i < shape.size(); ++i) {
    auto size = shape[i];
    auto st = stride[i];
    if (size == 1) {
      continue;
    }
    if (!view_dims.empty() && view_strides.back() == st * size) {
      view_dims.back() *= size;
    } else {
      view_dims.push_back(size);
      view_strides.push_back(st);
    }
  }
  if (view_dims.empty()) {
    return true;
  }
  return view_strides == contiguous_stride(view_dims);
}

std::vector<int64_t> compute_view_stride(const std::vector<int64_t>& shape,
                                         const std::vector<int64_t>& stride,
                                         const std::vector<int64_t>& new_shape) {
  if (!can_view(shape, stride, new_shape)) {
    throw std::runtime_error("View not compatible");
  }
  return contiguous_stride(new_shape);
}

std::pair<int64_t, int64_t> launch_config(int64_t total, int64_t threads = 256) {
  int64_t blocks = (total + threads - 1) / threads;
  return {blocks, threads};
}

at::Tensor launch_add(const at::Tensor& tensor, double value) {
  auto total = tensor.numel();
  auto contiguous = tensor.is_contiguous();
  (void)contiguous;
  launch_config(total);
  return tensor.add(value);
}

at::Tensor reshape_with_checks(const at::Tensor& tensor, const std::vector<int64_t>& shape) {
  auto sizes = tensor.sizes().vec();
  auto strides = tensor.strides().vec();
  auto inferred = infer_size(tensor.numel(), shape);
  auto target_stride = compute_view_stride(sizes, strides, inferred);
  return tensor.as_strided(inferred, target_stride);
}

at::Tensor emulate_chain(const at::Tensor& tensor,
                         const std::vector<int64_t>& shape_a,
                         const std::vector<int64_t>& shape_b) {
  auto out = launch_add(tensor, 1.0);
  out = reshape_with_checks(out, shape_a);
  out = launch_add(out, -1.0);
  out = reshape_with_checks(out, shape_b);
  out = launch_add(out, 0.0);
  return out;
}
}  // namespace

int main() {
  const std::vector<int64_t> shape_a = {19, 17, 13, 11, 7, 5, 3, 2};
  const std::vector<int64_t> shape_b = {2, 3, 5, 7, 11, 13, 17, 19};
  const int64_t loops = 100;

  auto options = torch::TensorOptions().device(torch::kCUDA).dtype(torch::kFloat32);
  auto tensor = torch::empty(shape_b, options);

  auto start = std::chrono::high_resolution_clock::now();
  for (int64_t i = 0; i < loops; ++i) {
    auto out = emulate_chain(tensor, shape_a, shape_b);
    (void)out;
  }
  auto end = std::chrono::high_resolution_clock::now();
  auto duration = std::chrono::duration_cast<std::chrono::duration<double>>(end - start);
  std::cout << "method4_custom_seconds=" << duration.count() << std::endl;
  return 0;
}
