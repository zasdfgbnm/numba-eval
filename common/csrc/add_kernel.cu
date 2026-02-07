#include <cuda.h>
#include <cuda_runtime.h>
#include <stdint.h>
#include <c10/cuda/CUDAStream.h>

__global__ void add_kernel(const float* __restrict__ input,
                           float* __restrict__ output,
                           int64_t numel, float alpha) {
  constexpr int vec_size = 4;
  int64_t tid = static_cast<int64_t>(blockIdx.x) * blockDim.x + threadIdx.x;
  int64_t stride = static_cast<int64_t>(gridDim.x) * blockDim.x;
  int64_t vec_numel = numel / vec_size;

  // Vectorized grid-stride loop: process 4 floats per iteration via float4.
  for (int64_t i = tid; i < vec_numel; i += stride) {
    float4 in = reinterpret_cast<const float4*>(input)[i];
    float4 out;
    out.x = in.x + alpha;
    out.y = in.y + alpha;
    out.z = in.z + alpha;
    out.w = in.w + alpha;
    reinterpret_cast<float4*>(output)[i] = out;
  }

  // Handle remaining elements (numel not divisible by 4).
  int64_t tail_start = vec_numel * vec_size;
  for (int64_t i = tail_start + tid; i < numel; i += stride) {
    output[i] = input[i] + alpha;
  }
}

extern "C" __attribute__((visibility("default"))) void add(
    const float* input,
    float* output,
    int64_t numel,
    float alpha) {
  constexpr int threads = 128;
  constexpr int vec_size = 4;
  // Size grid so each thread processes at least 2 float4 loads (8 elements),
  // matching LibTorch's vectorized_elementwise_kernel grid sizing.
  constexpr int elems_per_thread = vec_size * 2;
  int blocks = static_cast<int>((numel + threads * elems_per_thread - 1) /
                                (threads * elems_per_thread));
  if (blocks == 0) blocks = 1;
  cudaStream_t stream = at::cuda::getCurrentCUDAStream().stream();
  add_kernel<<<blocks, threads, 0, stream>>>(input, output, numel, alpha);
}
