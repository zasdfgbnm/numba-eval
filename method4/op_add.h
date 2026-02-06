#pragma once

#include <torch/torch.h>

#include "common_kernel.h"

at::Tensor launch_add(const at::Tensor& tensor, float value, LaunchAddKernelFn kernel);

