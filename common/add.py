from libcommon import add as _c_add  # type: ignore[import-not-found]
from allocate import allocate
from tensor_view import TensorView


def _check_contiguous(shape: tuple[int, ...], stride: tuple[int, ...]) -> int:
    if len(shape) != len(stride):
        raise ValueError(
            f"shape/stride rank mismatch: {len(shape)} vs {len(stride)}"
        )
    expected = 1
    numel = 1
    for dim, st in zip(reversed(shape), reversed(stride)):
        if int(st) != expected:
            raise ValueError(
                f"non-contiguous view: shape={shape} stride={stride}"
            )
        expected *= int(dim)
        numel *= int(dim)
    return int(numel)


def add(inp: TensorView, value: float) -> TensorView:
    """Allocate a new temp buffer and run add into it."""
    numel = _check_contiguous(inp.shape, inp.stride)
    out_ptr = allocate(numel * 4)  # float32
    _c_add(inp.ptr, out_ptr, numel, value)
    return TensorView(ptr=out_ptr, shape=inp.shape, stride=inp.stride)
