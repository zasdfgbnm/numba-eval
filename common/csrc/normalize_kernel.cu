#include <cuda.h>
#include <cuda_runtime.h>
#include <math.h>
#include <stdint.h>
#include <c10/cuda/CUDAStream.h>

// Each thread handles one vector. Two-pass but with minimal register pressure.
// The reduce dims are small (11-19) so the second read hits L1/L2.
__global__ void normalize_kernel(const float* __restrict__ input,
                                 float* __restrict__ output,
                                 int num_vectors,
                                 int reduce_dim_size,
                                 int dim_stride) {
  int tid = blockIdx.x * blockDim.x + threadIdx.x;
  int grid_stride = gridDim.x * blockDim.x;
  int inner_size = dim_stride;

  for (int v = tid; v < num_vectors; v += grid_stride) {
    int outer = v / inner_size;
    int inner = v - outer * inner_size;
    int base = outer * dim_stride * reduce_dim_size + inner;

    // Pass 1: sum of squares.
    float sum_sq = 0.0f;
    #pragma unroll 4
    for (int k = 0; k < reduce_dim_size; ++k) {
      float val = __ldg(&input[base + k * dim_stride]);
      sum_sq += val * val;
    }

    float inv_norm = rsqrtf(fmaxf(sum_sq, 1e-24f));

    // Pass 2: normalize and write.
    #pragma unroll 4
    for (int k = 0; k < reduce_dim_size; ++k) {
      int idx = base + k * dim_stride;
      output[idx] = __ldg(&input[idx]) * inv_norm;
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
  // Ensure each thread does >= 2 iterations, matching LibTorch grid sizing.
  blocks = (blocks + 1) >> 1;
  if (blocks == 0) blocks = 1;
  cudaStream_t stream = at::cuda::getCurrentCUDAStream().stream();
  normalize_kernel<<<blocks, threads, 0, stream>>>(
      input, output, n_vectors,
      static_cast<int>(reduce_dim_size),
      static_cast<int>(dim_stride));
}
