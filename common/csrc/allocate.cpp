#include <cstdint>
#include <unordered_map>

#include <ATen/ATen.h>
#include <c10/core/DeviceType.h>

namespace {
enum class DeviceType : int { CPU = 0, CUDA = 1 };

#if defined(NUMBA_EVAL_ALLOCATE_DEVICE_CUDA)
constexpr DeviceType kDevice = DeviceType::CUDA;
#else
constexpr DeviceType kDevice = DeviceType::CPU;
#endif

// Thread-local ownership map: `allocate_buf` and `free_buf` must be called on
// the same thread.
thread_local std::unordered_map<uint64_t, at::Tensor> g_buffers;

at::TensorOptions buffer_options() {
  if constexpr (kDevice == DeviceType::CUDA) {
    return at::TensorOptions().device(c10::kCUDA).dtype(at::kByte);
  }
  return at::TensorOptions().device(c10::kCPU).dtype(at::kByte);
}
}  // namespace

// Allocate a temporary buffer as a 1D uint8 tensor, and return its raw data pointer.
// Ownership is maintained by `g_buffers` until `free_buf(ptr)` is called.
extern "C" __attribute__((visibility("default"))) uint64_t allocate_buf(int64_t num_bytes) {
  auto tensor = at::empty({num_bytes}, buffer_options());
  uint64_t ptr = reinterpret_cast<uint64_t>(tensor.data_ptr<uint8_t>());
  g_buffers[ptr] = std::move(tensor);
  return ptr;
}

extern "C" __attribute__((visibility("default"))) void free_buf(uint64_t ptr) {
  g_buffers.erase(ptr);
}

