#include "chain.h"

#include <torch/torch.h>
#include <vector>

namespace F = torch::nn::functional;

void method2_libtorch_chain(const at::Tensor& tensor) {
  const std::vector<int64_t> shape_a = {19, 17, 13, 11, 7, 5, 3, 2};
  const std::vector<int64_t> shape_b = {2, 3, 5, 7, 11, 13, 17, 19};

  // Match benchmark intent: focus on dispatch/overhead, not autograd.
  torch::NoGradGuard no_grad;

  auto out = tensor;
  for (int64_t i = 0; i < 100; ++i) {
    out = out.reshape(shape_a);
    out = F::normalize(out, F::NormalizeFuncOptions().dim(i % 4));
    out = out.reshape(shape_b);
  }
}
