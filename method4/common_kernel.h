#pragma once

#include <cstdint>

using LaunchAddKernelFn = void (*)(const float*, float*, int64_t, float);
using NormalizeKernelFn = void (*)(const float*, float*, int64_t, int64_t, int64_t);
using AllocateBufFn = uint64_t (*)(int64_t);
using FreeBufFn = void (*)(uint64_t);

struct CommonApi {
  void* handle = nullptr;  // keep dlopen alive
  LaunchAddKernelFn add = nullptr;
  NormalizeKernelFn normalize = nullptr;
  AllocateBufFn allocate_buf = nullptr;
  FreeBufFn free_buf = nullptr;
};

CommonApi load_common_api();
