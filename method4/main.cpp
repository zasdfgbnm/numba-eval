#include <chrono>
#include <iostream>
#include <string>
#include <tuple>
#include <torch/torch.h>
#include <vector>

#include "common_kernel.h"
#include "op_add.h"
#include "op_reshape.h"

namespace {
torch::Device parse_device(int argc, char** argv) {
  // Simple flag parser: --device cpu|cuda
  std::string device = "cpu";
  for (int i = 1; i + 1 < argc; ++i) {
    if (std::string(argv[i]) == "--device") {
      device = argv[i + 1];
    }
  }
  if (device == "cuda") {
    return torch::Device(torch::kCUDA);
  }
  return torch::Device(torch::kCPU);
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

int main(int argc, char** argv) {
  const std::vector<int64_t> shape_a = {19, 17, 13, 11, 7, 5, 3, 2};
  const std::vector<int64_t> shape_b = {2, 3, 5, 7, 11, 13, 17, 19};
  const int64_t loops = 100;

  const auto dev = parse_device(argc, argv);
  auto options = torch::TensorOptions().device(dev).dtype(torch::kFloat32);
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
