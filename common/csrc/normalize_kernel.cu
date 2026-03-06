#include <cuda.h>
#include <cuda_runtime.h>
#include <math.h>
#include <stdint.h>
#include <c10/cuda/CUDAStream.h>

// Each thread handles one "vector" (one independent reduction group).
// A vector has `reduce_dim_size` elements spaced `dim_stride` apart.
// There are `num_vectors = numel / reduce_dim_size` independent vectors.
// Vector index v maps to a base offset:
//   outer = v / inner_size
//   inner = v % inner_size
//   base  = outer * dim_stride * reduce_dim_size + inner
__global__ void normalize_kernel(const float* __restrict__ input,
                                 float* __restrict__ output,
                                 int num_vectors,
                                 int reduce_dim_size,
                                 int dim_stride) {
  int vid = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = gridDim.x * blockDim.x;

  for (int v = vid; v < num_vectors; v += stride) {
    int inner_size = dim_stride;
    int outer = v / inner_size;
    int inner = v - outer * inner_size;
    int base = outer * dim_stride * reduce_dim_size + inner;

    // Pass 1: compute sum of squares.
    float sum_sq = 0.0f;
    for (int k = 0; k < reduce_dim_size; ++k) {
      float val = input[base + k * dim_stride];
      sum_sq += val * val;
    }

    float norm = sqrtf(sum_sq);
    float inv_norm = 1.0f / fmaxf(norm, 1e-12f);

    // Pass 2: write normalized values.
    for (int k = 0; k < reduce_dim_size; ++k) {
      int idx = base + k * dim_stride;
      output[idx] = input[idx] * inv_norm;
    }
  }
}

extern "C" __attribute__((visibility("default"))) void normalize(
    const float* input,
    float* output,
    int64_t numel,
    int64_t reduce_dim_size,
    int64_t dim_stride) {
  int n_vectors = static_cast<int>(numel / reduce_dim_size);
  constexpr int threads = 128;
  int blocks = (n_vectors + threads - 1) / threads;
  blocks = (blocks + 1) >> 1;  // ensure >= 2 iterations per thread
  if (blocks == 0) blocks = 1;
  cudaStream_t stream = at::cuda::getCurrentCUDAStream().stream();
  normalize_kernel<<<blocks, threads, 0, stream>>>(
      input, output, n_vectors,
      static_cast<int>(reduce_dim_size),
      static_cast<int>(dim_stride));
}
