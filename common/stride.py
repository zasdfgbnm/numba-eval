import numpy as np
from numba import njit  # type: ignore[import-untyped]


def contiguous_stride(shape) -> np.ndarray:
    """Compute contiguous (row-major) stride for a 1D shape container.

    Returns an int64 ndarray of same length as `shape`.
    Accepts either a tuple/list of ints or an int64 ndarray.
    """
    n = len(shape)
    stride = np.empty(n, np.int64)
    if n == 0:
        return stride
    stride[n - 1] = 1
    for i in range(n - 2, -1, -1):
        stride[i] = int(stride[i + 1]) * int(shape[i + 1])
    return stride


contiguous_stride_jit = njit(contiguous_stride, cache=True)


__all__ = ["contiguous_stride", "contiguous_stride_jit"]
