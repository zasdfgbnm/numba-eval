#pragma once

#include <cstdint>
#include <string>

// Run the add/reshape chain inside LibTorch.
//
// Notes:
// - For CUDA tensors, this does NOT synchronize the device.
void run_method2_libtorch_chain(const std::string& device);

