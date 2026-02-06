import ctypes
import os

import torch  # type: ignore[import-not-found]

_COMMON_KERNEL: ctypes.CDLL | None = None


def _load_common_kernel() -> ctypes.CDLL:
    global _COMMON_KERNEL
    if _COMMON_KERNEL is not None:
        return _COMMON_KERNEL

    common_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "common"))
    candidates = [
        os.path.join(common_dir, "libcommon.so"),
        os.path.join(common_dir, "libcommon.dylib"),
    ]
    so_path = next((p for p in candidates if os.path.exists(p)), None)
    if so_path is None:
        raise FileNotFoundError(f"common kernel library not found. Tried: {candidates}")

    lib = ctypes.CDLL(so_path)
    lib.add1d.argtypes = [
        ctypes.c_uint64,
        ctypes.c_uint64,
        ctypes.c_int64,
        ctypes.c_float,
    ]
    lib.add1d.restype = None
    _COMMON_KERNEL = lib
    return lib


def launch_add(tensor: torch.Tensor, value: float) -> torch.Tensor:
    """Add a scalar value using the common kernel (CPU dylib or CUDA so)."""
    if tensor.dtype != torch.float32:
        raise TypeError(f"add1d expects float32 tensor, got {tensor.dtype}")

    numel = tensor.numel()
    output = torch.empty_like(tensor)
    kernel = _load_common_kernel()
    kernel.add1d(
        ctypes.c_uint64(tensor.data_ptr()),
        ctypes.c_uint64(output.data_ptr()),
        ctypes.c_int64(numel),
        ctypes.c_float(value),
    )
    return output
