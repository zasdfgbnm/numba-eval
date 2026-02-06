#pragma once

#include <cstdint>
#include <vector>

// Mirror method3: operate on (ptr, shape, stride).
struct TensorView {
  uint64_t ptr = 0;
  std::vector<int64_t> shape;
  std::vector<int64_t> stride;
};

