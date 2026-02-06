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

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("torch_cuda_empty", &torch_cuda_empty, "Allocate CUDA tensor (numel)");
  m.def("torch_cuda_data_ptr", &torch_cuda_data_ptr, "Get data pointer from handle");
  m.def("torch_cuda_release", &torch_cuda_release, "Release handle");
}
