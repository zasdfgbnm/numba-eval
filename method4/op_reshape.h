#pragma once

#include <cstdint>
#include <utility>
#include <vector>

std::pair<std::vector<int64_t>, std::vector<int64_t>> reshape_with_checks(
    const std::vector<int64_t>& shape,
    const std::vector<int64_t>& stride,
    const std::vector<int64_t>& target_shape);

