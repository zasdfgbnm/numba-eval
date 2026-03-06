#pragma once

#include <array>
#include <cstdint>

#include "common_kernel.h"
#include "tensor_view.h"

template <int Rank>
TensorView<Rank> normalize(const TensorView<Rank>& in, int64_t dim, const CommonApi& api);
