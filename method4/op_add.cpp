#include "op_add.h"

#include <cstdint>
#include <utility>

namespace {
std::pair<int64_t, int64_t> launch_config(int64_t total, int64_t threads = 256) {
  int64_t blocks = (total + threads - 1) / threads;
  return {blocks, threads};
}
}  // namespace

at::Tensor launch_add(const at::Tensor& tensor, float value, LaunchAddKernelFn kernel) {
  auto total = tensor.numel();
  (void)launch_config(total);
  auto output = torch::empty_like(tensor);
  kernel(tensor.data_ptr<float>(), output.data_ptr<float>(), total, value);
  return output;
}

