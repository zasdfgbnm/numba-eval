#pragma once

#include <cstdint>
#include <array>

// Mirror method3: operate on (ptr, shape, stride).
template <int Rank>
struct TensorView {
  static_assert(Rank >= 0, "Rank must be non-negative");

  uint64_t ptr = 0;
  std::array<int64_t, Rank> shape{};
  std::array<int64_t, Rank> stride{};
};

