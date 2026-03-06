from numba import njit  # type: ignore[import-untyped]

from libcommon import normalize as _c_normalize  # type: ignore[import-not-found]

from allocate import allocate, allocate_jit
from tensor_view import TensorView


def _get(jit: bool):
    def _check_contiguous(
        shape: tuple[int, ...], stride: tuple[int, ...]
    ) -> int:
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
        _check_contiguous = njit(
            _check_contiguous, cache=True, inline="always"
        )

    _allocate = allocate_jit if jit else allocate

    def normalize(inp: TensorView, dim: int) -> TensorView:
        """Allocate a new buffer and run L2 normalize along dim into it."""
        numel = int(_check_contiguous(inp.shape, inp.stride))
        out_ptr = int(_allocate(int(numel) * 4))  # float32 bytes
        reduce_dim_size = int(inp.shape[dim])
        # dim_stride = product of shape[dim+1 .. rank-1] = contiguous stride of dim
        dim_stride = 1
        for d in range(int(dim) + 1, len(inp.shape)):
            dim_stride *= int(inp.shape[d])
        _c_normalize(int(inp.ptr), int(out_ptr), int(numel),
                     int(reduce_dim_size), int(dim_stride))
        return TensorView(ptr=int(out_ptr), shape=inp.shape, stride=inp.stride)

    if jit:
        normalize = njit(normalize, cache=True, inline="always")

    return normalize


normalize = _get(False)
normalize_jit = _get(True)

__all__ = ["normalize", "normalize_jit"]
