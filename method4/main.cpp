#include <chrono>
#include <cstdlib>
#include <dlfcn.h>
#include <iostream>
#include <numeric>
#include <torch/torch.h>

using LaunchAddKernelFn = void (*)(const float*, float*, int64_t, float);

LaunchAddKernelFn load_common_kernel() {
  const char* env_path = std::getenv("NUMBA_EVAL_COMMON_SO");
  std::string so_path = env_path ? env_path : "common/libcommon.so";
  void* handle = dlopen(so_path.c_str(), RTLD_LAZY);
  if (!handle) {
    throw std::runtime_error("Failed to load common.so: " + so_path);
  }
  auto fn = reinterpret_cast<LaunchAddKernelFn>(dlsym(handle, "common_launch_add_kernel"));
  if (!fn) {
    throw std::runtime_error("Failed to find common_launch_add_kernel");
  }
  return fn;
}

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

  for (int64_t tensor_dim = static_cast<int64_t>(shape.size()) - 1; tensor_dim >= 0; --tensor_dim) {
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

std::pair<int64_t, int64_t> launch_config(int64_t total, int64_t threads = 256) {
  int64_t blocks = (total + threads - 1) / threads;
  return {blocks, threads};
}

at::Tensor launch_add(const at::Tensor& tensor, float value, LaunchAddKernelFn kernel) {
  auto total = tensor.numel();
  launch_config(total);
  auto output = torch::empty_like(tensor);
  kernel(tensor.data_ptr<float>(), output.data_ptr<float>(), total, value);
  return output;
}

std::pair<std::vector<int64_t>, std::vector<int64_t>> reshape_with_checks(
    const std::vector<int64_t>& shape,
    const std::vector<int64_t>& stride,
    const std::vector<int64_t>& target_shape) {
  auto inferred = infer_size(numel(shape), target_shape);
  auto target_stride = compute_view_stride(shape, stride, inferred);
  return {inferred, target_stride};
}

at::Tensor emulate_chain(const at::Tensor& tensor,
                         const std::vector<int64_t>& shape_a,
                         const std::vector<int64_t>& shape_b,
                         LaunchAddKernelFn kernel) {
  auto flat = tensor.view({tensor.numel()});
  std::vector<int64_t> shape = {flat.numel()};
  std::vector<int64_t> stride = {1};

  flat = launch_add(flat, 1.0f, kernel);
  std::tie(shape, stride) = reshape_with_checks(shape, stride, shape_a);
  flat = launch_add(flat, -1.0f, kernel);
  std::tie(shape, stride) = reshape_with_checks(shape, stride, shape_b);
  flat = launch_add(flat, 0.0f, kernel);

  auto options = tensor.options();
  auto output = torch::empty_strided(shape_b, stride, options);
  output.view({-1}).copy_(flat);
  return output;
}
}  // namespace

int main() {
  const std::vector<int64_t> shape_a = {19, 17, 13, 11, 7, 5, 3, 2};
  const std::vector<int64_t> shape_b = {2, 3, 5, 7, 11, 13, 17, 19};
  const int64_t loops = 100;

  auto options = torch::TensorOptions().device(torch::kCUDA).dtype(torch::kFloat32);
  auto tensor = torch::empty(shape_b, options);
  auto kernel = load_common_kernel();

  auto start = std::chrono::high_resolution_clock::now();
  auto out = tensor;
  for (int64_t i = 0; i < loops; ++i) {
    out = emulate_chain(out, shape_a, shape_b, kernel);
  }
  auto end = std::chrono::high_resolution_clock::now();
  auto duration = std::chrono::duration_cast<std::chrono::duration<double>>(end - start);
  std::cout << "method4_custom_seconds=" << duration.count() << std::endl;
  return 0;
}
