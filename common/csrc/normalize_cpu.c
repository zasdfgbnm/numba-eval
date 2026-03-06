#include <math.h>
#include <stdint.h>

// CPU implementation that matches the CUDA kernel ABI:
//   void normalize(const float* input, float* output,
//                  int64_t numel, int64_t reduce_dim_size, int64_t dim_stride)
__attribute__((visibility("default"))) void normalize(
    const float* input,
    float* output,
    int64_t numel,
    int64_t reduce_dim_size,
    int64_t dim_stride) {
  int64_t num_vectors = numel / reduce_dim_size;
  int64_t inner_size = dim_stride;

  for (int64_t v = 0; v < num_vectors; ++v) {
    int64_t outer = v / inner_size;
    int64_t inner = v - outer * inner_size;
    int64_t base = outer * dim_stride * reduce_dim_size + inner;

    float sum_sq = 0.0f;
    for (int64_t k = 0; k < reduce_dim_size; ++k) {
      float val = input[base + k * dim_stride];
      sum_sq += val * val;
    }

    float norm = sqrtf(sum_sq);
    float inv_norm = 1.0f / fmaxf(norm, 1e-12f);

    for (int64_t k = 0; k < reduce_dim_size; ++k) {
      int64_t idx = base + k * dim_stride;
      output[idx] = input[idx] * inv_norm;
    }
  }
}
