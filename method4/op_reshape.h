#pragma once

#include <cstdint>
#include <utility>
#include <vector>

#include "tensor_view.h"

// Mirror method3: reshape operates on TensorView metadata (ptr unchanged).
TensorView reshape(const TensorView& in, const std::vector<int64_t>& target_shape);

