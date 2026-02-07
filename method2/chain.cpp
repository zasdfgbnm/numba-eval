#include "chain.h"

#include <stdexcept>
#include <torch/torch.h>
#include <vector>

namespace {
constexpr int64_t kLoops = 100;

torch::Device parse_device_string(const std::string& device) {
  if (device == "cuda") {
    return torch::Device(torch::kCUDA);
  }
  if (device == "cpu") {
    return torch::Device(torch::kCPU);
  }
  throw std::invalid_argument("Unsupported device: " + device + " (expected 'cpu' or 'cuda')");
}
}  // namespace

void run_method2_libtorch_chain(const std::string& device) {
  const std::vector<int64_t> shape_a = {19, 17, 13, 11, 7, 5, 3, 2};
  const std::vector<int64_t> shape_b = {2, 3, 5, 7, 11, 13, 17, 19};

  const auto dev = parse_device_string(device);
  auto options = torch::TensorOptions().device(dev).dtype(torch::kFloat32);
  auto tensor = torch::empty(shape_b, options);

  // Match benchmark intent: focus on dispatch/overhead, not autograd.
  torch::NoGradGuard no_grad;

  auto out = tensor;
  for (int64_t i = 0; i < kLoops; ++i) {
    out = out.add(1);
    out = out.reshape(shape_a);
    out = out.add(-1);
    out = out.reshape(shape_b);
    out = out.add(0);
  }
}

