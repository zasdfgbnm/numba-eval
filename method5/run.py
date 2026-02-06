import argparse
import json
import os
import ctypes
from typing import Tuple

import torch  # type: ignore[import-not-found]

from numba_eval.benchmark import time_cpu  # type: ignore[import-untyped]


SHAPE_B = (2, 3, 5, 7, 11, 13, 17, 19)
LOOPS = 100

_COMMON_KERNEL = None


def _load_common_kernel() -> ctypes.CDLL:
    global _COMMON_KERNEL
    if _COMMON_KERNEL is not None:
        return _COMMON_KERNEL

    common_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "common")
    )
    candidates = [
        os.path.join(common_dir, "libcommon.so"),
        os.path.join(common_dir, "libcommon.dylib"),
    ]
    so_path = next((p for p in candidates if os.path.exists(p)), None)
    if so_path is None:
        raise FileNotFoundError(
            f"common kernel library not found. Tried: {candidates}"
        )

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


def _contiguous_stride(shape: Tuple[int, ...]) -> Tuple[int, ...]:
    stride = [1] * len(shape)
    for i in range(len(shape) - 2, -1, -1):
        stride[i] = stride[i + 1] * shape[i + 1]
    return tuple(stride)


def method5_bridge(tensor: torch.Tensor, use_numba: bool) -> Tuple[float, str]:
    ext_path = os.environ.get("NUMBA_EVAL_BRIDGE")
    if not ext_path or not os.path.exists(ext_path):
        return float("nan"), "bridge library not found (set NUMBA_EVAL_BRIDGE)"

    bridge = ctypes.CDLL(ext_path)
    bridge.torch_cuda_empty.argtypes = [ctypes.c_int64]
    bridge.torch_cuda_empty.restype = ctypes.c_int64
    bridge.torch_cuda_data_ptr.argtypes = [ctypes.c_int64]
    bridge.torch_cuda_data_ptr.restype = ctypes.c_uint64

    kernel = _load_common_kernel()

    def op() -> None:
        _handle = bridge.torch_cuda_empty(tensor.numel())
        in_ptr = tensor.data_ptr()
        out_tensor = torch.empty_strided(
            SHAPE_B,
            _contiguous_stride(SHAPE_B),
            device=tensor.device,
            dtype=tensor.dtype,
        )
        out_ptr = out_tensor.data_ptr()
        for _ in range(LOOPS):
            kernel.add1d(
                ctypes.c_uint64(in_ptr),
                ctypes.c_uint64(out_ptr),
                ctypes.c_int64(tensor.numel()),
                ctypes.c_float(1.0),
            )
            kernel.add1d(
                ctypes.c_uint64(out_ptr),
                ctypes.c_uint64(out_ptr),
                ctypes.c_int64(tensor.numel()),
                ctypes.c_float(-1.0),
            )
            kernel.add1d(
                ctypes.c_uint64(out_ptr),
                ctypes.c_uint64(out_ptr),
                ctypes.c_int64(tensor.numel()),
                ctypes.c_float(0.0),
            )
            in_ptr = out_ptr

    if use_numba:
        try:
            import numba  # type: ignore[import-not-found]  # noqa: F401
        except Exception as exc:  # pragma: no cover - environment dependent
            return float("nan"), f"numba unavailable: {exc}"

    return time_cpu(op, 1), "ok"


def method5_ctypes_cpu(tensor: torch.Tensor) -> float:
    """CPU-only fallback: call add1d via ctypes on CPU tensors."""
    if tensor.device.type != "cpu":
        raise RuntimeError("method5_ctypes_cpu expects a CPU tensor")
    if tensor.dtype != torch.float32:
        raise TypeError(f"add1d expects float32 tensor, got {tensor.dtype}")

    kernel = _load_common_kernel()
    out = torch.empty_like(tensor)

    def op() -> None:
        in_ptr = tensor.data_ptr()
        out_ptr = out.data_ptr()
        for _ in range(LOOPS):
            kernel.add1d(
                ctypes.c_uint64(in_ptr),
                ctypes.c_uint64(out_ptr),
                ctypes.c_int64(tensor.numel()),
                ctypes.c_float(1.0),
            )
            kernel.add1d(
                ctypes.c_uint64(out_ptr),
                ctypes.c_uint64(out_ptr),
                ctypes.c_int64(tensor.numel()),
                ctypes.c_float(-1.0),
            )
            kernel.add1d(
                ctypes.c_uint64(out_ptr),
                ctypes.c_uint64(out_ptr),
                ctypes.c_int64(tensor.numel()),
                ctypes.c_float(0.0),
            )

    return time_cpu(op, 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device)
    tensor = torch.empty(SHAPE_B, device=device, dtype=torch.float32)

    if device.type == "cuda":
        results: dict[str, float | str] = {}
        time5a, note5a = method5_bridge(tensor, use_numba=True)
        results["method5a_bridge_numba"] = time5a
        results["method5a_note"] = note5a

        time5b, note5b = method5_bridge(tensor, use_numba=False)
        results["method5b_bridge_python"] = time5b
        results["method5b_note"] = note5b

        print(json.dumps(results, indent=2))
        return

    # CPU-only fallback path.
    result = {"method5_ctypes_cpu": method5_ctypes_cpu(tensor)}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
