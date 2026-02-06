#include <cuda.h>
#include <cuda_runtime.h>
#include <stdint.h>

__global__ void add_kernel(const float* input, float* output, int64_t numel, float alpha) {
  int64_t idx = static_cast<int64_t>(blockIdx.x) * blockDim.x + threadIdx.x;
  if (idx < numel) {
    output[idx] = input[idx] + alpha;
  }
}

extern "C" __attribute__((visibility("default"))) void add1d(
    const float* input,
    float* output,
    int64_t numel,
    float alpha) {
  const int threads = 256;
  const int blocks = static_cast<int>((numel + threads - 1) / threads);
  add_kernel<<<blocks, threads>>>(input, output, numel, alpha);
}
