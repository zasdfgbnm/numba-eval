#include <chrono>
#include <iostream>
#include <torch/torch.h>

int main() {
  const std::vector<int64_t> shape_a = {19, 17, 13, 11, 7, 5, 3, 2};
  const std::vector<int64_t> shape_b = {2, 3, 5, 7, 11, 13, 17, 19};
  const int64_t loops = 100;

  auto options = torch::TensorOptions().device(torch::kCUDA).dtype(torch::kFloat32);
  auto tensor = torch::empty(shape_b, options);

  auto start = std::chrono::high_resolution_clock::now();
  for (int64_t i = 0; i < loops; ++i) {
    auto out = tensor.add(1);
    out = out.reshape(shape_a);
    out = out.add(-1);
    out = out.reshape(shape_b);
    out = out.add(0);
    (void)out;
  }
  auto end = std::chrono::high_resolution_clock::now();
  auto duration = std::chrono::duration_cast<std::chrono::duration<double>>(end - start);
  std::cout << "method2_libtorch_seconds=" << duration.count() << std::endl;
  return 0;
}
