from numba import njit  # type: ignore[import-untyped]

from tuple_utils import tuple_set_item


def contiguous_stride(shape: tuple[int, ...]) -> tuple[int, ...]:
    """Compute contiguous (row-major) stride for a shape tuple.

    Returns a tuple of same length as `shape`.
    """
    n = len(shape)
    if n == 0:
        return ()

    # Numba does not support tuple * int at runtime; start from a same-length
    # tuple (the input `shape`) and overwrite all elements.
    stride = shape
    stride = tuple_set_item(stride, int(n - 1), 1)
    for i in range(n - 2, -1, -1):
        stride = tuple_set_item(
            stride,
            int(i),
            int(stride[i + 1]) * int(shape[i + 1]),
        )
    return stride


contiguous_stride_jit = njit(contiguous_stride, cache=True, inline="always")


__all__ = ["contiguous_stride", "contiguous_stride_jit"]
