#pragma once

#include <cstdint>
#include <array>

#include "tensor_view.h"

// Mirror method3: reshape operates on TensorView metadata (ptr unchanged).
template <int InRank, int OutRank>
TensorView<OutRank> reshape(const TensorView<InRank>& in,
                            const std::array<int64_t, OutRank>& target_shape);

