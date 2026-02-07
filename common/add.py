import numpy as np
from numba import njit  # type: ignore[import-untyped]

from libcommon import add as _c_add  # type: ignore[import-not-found]

from allocate import allocate, allocate_jit
from tensor_view import TensorView


def _get(jit: bool):
    def _check_contiguous(
        shape: tuple[int, ...], stride: tuple[int, ...]
    ) -> int:
        # Keep error messages JIT-friendly (no f-strings).
        if len(shape) != len(stride):
            raise ValueError("shape/stride rank mismatch")
        expected = 1
        numel = 1
        for i in range(len(shape) - 1, -1, -1):
            dim = int(shape[i])
            st = int(stride[i])
            if st != expected:
                raise ValueError("non-contiguous view")
            expected *= dim
            numel *= dim
        return int(numel)

    if jit:
        _check_contiguous = njit(_check_contiguous, cache=True)

    _allocate = allocate_jit if jit else allocate

    def add(inp: TensorView, value: float) -> TensorView:
        """Allocate a new temp buffer and run add into it."""
        numel = int(_check_contiguous(inp.shape, inp.stride))
        out_ptr = int(_allocate(int(numel) * 4))  # float32 bytes
        _c_add(int(inp.ptr), int(out_ptr), int(numel), np.float32(value))
        return TensorView(ptr=int(out_ptr), shape=inp.shape, stride=inp.stride)

    if jit:
        add = njit(add, cache=True)

    return add


add = _get(False)
add_jit = _get(True)

__all__ = ["add", "add_jit"]
