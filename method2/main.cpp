#include <chrono>
#include <iostream>
#include <string>
#include <torch/torch.h>

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
}  // namespace

int main(int argc, char** argv) {
  const std::vector<int64_t> shape_a = {19, 17, 13, 11, 7, 5, 3, 2};
  const std::vector<int64_t> shape_b = {2, 3, 5, 7, 11, 13, 17, 19};
  const int64_t loops = 100;

  const auto dev = parse_device(argc, argv);
  auto options = torch::TensorOptions().device(dev).dtype(torch::kFloat32);
  auto tensor = torch::empty(shape_b, options);

  auto start = std::chrono::high_resolution_clock::now();
  auto out = tensor;
  for (int64_t i = 0; i < loops; ++i) {
    out = out.add(1);
    out = out.reshape(shape_a);
    out = out.add(-1);
    out = out.reshape(shape_b);
    out = out.add(0);
  }
  auto end = std::chrono::high_resolution_clock::now();
  auto duration = std::chrono::duration_cast<std::chrono::duration<double>>(end - start);
  std::cout << "method2_libtorch_seconds=" << duration.count() << std::endl;
  return 0;
}
