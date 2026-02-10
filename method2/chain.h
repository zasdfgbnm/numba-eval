#pragma once

#include <cstdint>
#include <string>

#include <torch/torch.h>

// Run the add/reshape chain inside LibTorch on a pre-allocated tensor.
//
// Notes:
// - For CUDA tensors, this does NOT synchronize the device.
void method2_libtorch_chain(const at::Tensor& tensor);
