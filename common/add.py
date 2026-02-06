import ctypes
import math

from _C import _C
from allocate import allocate
from tensor_view import TensorView


def _check_contiguous(shape: tuple[int, ...], stride: tuple[int, ...]) -> int:
    if len(shape) != len(stride):
        raise ValueError(
            f"shape/stride rank mismatch: {len(shape)} vs {len(stride)}"
        )
    expected = 1
    for dim, st in zip(reversed(shape), reversed(stride)):
        if int(st) != expected:
            raise ValueError(
                f"non-contiguous view: shape={shape} stride={stride}"
            )
        expected *= int(dim)
    return int(math.prod(shape))


def add(inp: TensorView, value: float) -> TensorView:
    """Allocate a new temp buffer and run add into it."""
    numel = _check_contiguous(inp.shape, inp.stride)
    out_ptr = allocate(numel * 4)  # float32
    _C.add(
        ctypes.c_uint64(inp.ptr),
        ctypes.c_uint64(out_ptr),
        ctypes.c_int64(numel),
        ctypes.c_float(value),
    )
    return TensorView(ptr=out_ptr, shape=inp.shape, stride=inp.stride)
