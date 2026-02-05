#include <torch/extension.h>
#include <vector>

namespace {
std::vector<at::Tensor> g_tensors;
}

extern "C" __attribute__((visibility("default"))) int64_t torch_cuda_empty(int64_t numel) {
  auto options = torch::TensorOptions().device(torch::kCUDA).dtype(torch::kFloat32);
  auto tensor = torch::empty({numel}, options);
  g_tensors.emplace_back(tensor);
  return static_cast<int64_t>(g_tensors.size() - 1);
}

extern "C" __attribute__((visibility("default"))) uint64_t torch_cuda_data_ptr(int64_t handle) {
  if (handle < 0 || static_cast<size_t>(handle) >= g_tensors.size()) {
    return 0;
  }
  return reinterpret_cast<uint64_t>(g_tensors[handle].data_ptr());
}

extern "C" __attribute__((visibility("default"))) void torch_cuda_release(int64_t handle) {
  if (handle < 0 || static_cast<size_t>(handle) >= g_tensors.size()) {
    return;
  }
  g_tensors[handle] = at::Tensor();
}

void launch_add_kernel(const float* input, float* output, int64_t numel, float alpha);

extern "C" __attribute__((visibility("default"))) void torch_cuda_launch_add(
    uint64_t in_ptr,
    uint64_t out_ptr,
    int64_t numel,
    float alpha) {
  auto input = reinterpret_cast<const float*>(in_ptr);
  auto output = reinterpret_cast<float*>(out_ptr);
  launch_add_kernel(input, output, numel, alpha);
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("torch_cuda_empty", &torch_cuda_empty, "Allocate CUDA tensor (numel)");
  m.def("torch_cuda_data_ptr", &torch_cuda_data_ptr, "Get data pointer from handle");
  m.def("torch_cuda_release", &torch_cuda_release, "Release handle");
  m.def("torch_cuda_launch_add", &torch_cuda_launch_add, "Launch add kernel");
}
