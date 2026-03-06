"""Custom torch op wrapping libcommon's single-kernel L2 normalize.

Usage (eager or torch.compile):

    import custom_normalize_op  # registers torch.ops.numba_eval.normalize
    out = torch.ops.numba_eval.normalize(tensor, dim)
"""

import ctypes
import os

import torch

_common_dir = os.path.abspath(os.path.dirname(__file__))
_lib_path = os.path.join(_common_dir, "lib", "libcommon.so")
if not os.path.exists(_lib_path):
    _lib_path = os.path.join(_common_dir, "lib", "libcommon.dylib")
_lib = ctypes.CDLL(_lib_path)
_lib.normalize.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_int64,
    ctypes.c_int64,
    ctypes.c_int64,
]
_lib.normalize.restype = None


@torch.library.custom_op("numba_eval::normalize", mutates_args=())
def custom_normalize(input: torch.Tensor, dim: int) -> torch.Tensor:
    output = torch.empty_like(input)
    numel = input.numel()
    reduce_dim_size = input.shape[dim]
    dim_stride = 1
    for d in range(dim + 1, input.ndim):
        dim_stride *= input.shape[d]
    _lib.normalize(
        input.data_ptr(), output.data_ptr(), numel, reduce_dim_size, dim_stride
    )
    return output


@custom_normalize.register_fake
def _(input: torch.Tensor, dim: int) -> torch.Tensor:
    return torch.empty_like(input)
