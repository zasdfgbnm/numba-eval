#pragma once

#include <cstdint>

using LaunchAddKernelFn = void (*)(const float*, float*, int64_t, float);

LaunchAddKernelFn load_common_kernel();

