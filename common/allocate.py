import ctypes

from _C import _C


def allocate(num_bytes: int) -> int:
    """Allocate `num_bytes` and return a raw data pointer (uint64)."""
    if not isinstance(num_bytes, int):
        raise TypeError(f"num_bytes must be int, got {type(num_bytes)}")
    if num_bytes < 0:
        raise ValueError(f"num_bytes must be >= 0, got {num_bytes}")

    return int(_C.allocate_buf(num_bytes))


def free(ptr: int) -> None:
    """Release a pointer previously returned by `allocate`."""
    _C.free_buf(ctypes.c_uint64(ptr))
