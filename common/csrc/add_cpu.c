#include <stdint.h>

// CPU implementation that matches the CUDA kernel ABI:
//   void func(const float* input, float* output, int64_t numel, float alpha)
//
// This is intentionally simple: it's meant for measuring call overhead and
// validating Numba ExternalFunction calls on machines without CUDA.
__attribute__((visibility("default"))) void add1d(
    const float* input,
    float* output,
    int64_t numel,
    float alpha) {
  for (int64_t i = 0; i < numel; i++) {
    output[i] = input[i] + alpha;
  }
}
