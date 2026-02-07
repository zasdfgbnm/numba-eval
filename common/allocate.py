from numba import njit  # type: ignore[import-untyped]

from libcommon import allocate_buf, free_buf  # type: ignore[import-not-found]


def _get(jit: bool):
    def allocate(num_bytes: int) -> int:
        """Allocate `num_bytes` and return a raw data pointer (intp)."""
        if num_bytes < 0:
            raise ValueError("num_bytes must be >= 0")
        return int(allocate_buf(int(num_bytes)))

    if jit:
        allocate = njit(allocate, cache=True, inline="always")

    def free(ptr: int) -> None:
        """Release a pointer previously returned by `allocate`."""
        free_buf(int(ptr))

    if jit:
        free = njit(free, cache=True, inline="always")

    return allocate, free


allocate, free = _get(False)
allocate_jit, free_jit = _get(True)

__all__ = ["allocate", "free", "allocate_jit", "free_jit"]
