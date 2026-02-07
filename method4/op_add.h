#pragma once

#include <array>

#include "common_kernel.h"
#include "tensor_view.h"

template <int Rank>
TensorView<Rank> add(const TensorView<Rank>& in, float value, const CommonApi& api);

