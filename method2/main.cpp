#include <chrono>
#include <cstdlib>
#include <dlfcn.h>
#include <iostream>
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

at::Tensor launch_add(const at::Tensor& tensor, float value, LaunchAddKernelFn kernel) {
  auto output = torch::empty_like(tensor);
  kernel(tensor.data_ptr<float>(), output.data_ptr<float>(), tensor.numel(), value);
  return output;
}

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
    out = launch_add(out, 1.0f, kernel);
    out = out.reshape(shape_a);
    out = launch_add(out, -1.0f, kernel);
    out = out.reshape(shape_b);
    out = launch_add(out, 0.0f, kernel);
  }
  auto end = std::chrono::high_resolution_clock::now();
  auto duration = std::chrono::duration_cast<std::chrono::duration<double>>(end - start);
  std::cout << "method2_libtorch_seconds=" << duration.count() << std::endl;
  return 0;
}
