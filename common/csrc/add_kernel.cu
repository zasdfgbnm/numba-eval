#include <cuda.h>
#include <cuda_runtime.h>
#include <stdint.h>
#include <c10/cuda/CUDAStream.h>

__global__ void add_kernel(const float* __restrict__ input,
                           float* __restrict__ output,
                           int numel, float alpha) {
  int tid = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = gridDim.x * blockDim.x;
  int vec_numel = numel >> 2;

  // Vectorized grid-stride loop: process 4 floats per iteration via float4.
  #pragma unroll 2
  for (int i = tid; i < vec_numel; i += stride) {
    float4 in = reinterpret_cast<const float4*>(input)[i];
    float4 out;
    out.x = in.x + alpha;
    out.y = in.y + alpha;
    out.z = in.z + alpha;
    out.w = in.w + alpha;
    reinterpret_cast<float4*>(output)[i] = out;
  }

  // Handle remaining elements (numel not divisible by 4).
  for (int i = (vec_numel << 2) + tid; i < numel; i += stride) {
    output[i] = input[i] + alpha;
  }
}

extern "C" __attribute__((visibility("default"))) void add(
    const float* input,
    float* output,
    int64_t numel,
    float alpha) {
  constexpr int threads = 128;
  int n = static_cast<int>(numel);
  int vec_numel = n >> 2;
  int blocks = (vec_numel + threads - 1) / threads;
  // Ensure each thread does >= 2 iterations, matching LibTorch grid sizing.
  blocks = (blocks + 1) >> 1;
  if (blocks == 0) blocks = 1;
  cudaStream_t stream = at::cuda::getCurrentCUDAStream().stream();
  add_kernel<<<blocks, threads, 0, stream>>>(input, output, n, alpha);
}
