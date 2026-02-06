import argparse
import json
import os
import ctypes

import torch

from numba_eval.benchmark import time_cpu


SHAPE_A = (19, 17, 13, 11, 7, 5, 3, 2)
SHAPE_B = (2, 3, 5, 7, 11, 13, 17, 19)
LOOPS = 100

_COMMON_KERNEL = None


def _load_common_kernel() -> ctypes.CDLL:
    global _COMMON_KERNEL
    if _COMMON_KERNEL is not None:
        return _COMMON_KERNEL
    default_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "common", "libcommon.so"))
    so_path = os.environ.get("NUMBA_EVAL_COMMON_SO", default_path)
    if not os.path.exists(so_path):
        raise FileNotFoundError(f"common.so not found at {so_path}")
    lib = ctypes.CDLL(so_path)
    lib.common_launch_add_kernel.argtypes = [
        ctypes.c_uint64,
        ctypes.c_uint64,
        ctypes.c_int64,
        ctypes.c_float,
    ]
    lib.common_launch_add_kernel.restype = None
    _COMMON_KERNEL = lib
    return lib


def _launch_add(tensor: torch.Tensor, value: float) -> torch.Tensor:
    if tensor.device.type != "cuda":
        raise RuntimeError("CUDA tensor required for common kernel")
    output = torch.empty_like(tensor)
    kernel = _load_common_kernel()
    kernel.common_launch_add_kernel(
        ctypes.c_uint64(tensor.data_ptr()),
        ctypes.c_uint64(output.data_ptr()),
        ctypes.c_int64(tensor.numel()),
        ctypes.c_float(value),
    )
    return output


def method1_pytorch(tensor: torch.Tensor) -> float:
    def op() -> None:
        out = tensor
        for _ in range(LOOPS):
            out = _launch_add(out, 1.0)
            out = out.reshape(*SHAPE_A)
            out = _launch_add(out, -1.0)
            out = out.reshape(*SHAPE_B)
            out = _launch_add(out, 0.0)

    return time_cpu(op, 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device)
    if device.type != "cuda":
        print(json.dumps({"method1_error": "method1 requires CUDA for common kernel"}, indent=2))
        return

    tensor = torch.empty(SHAPE_B, device=device, dtype=torch.float32)
    result = {"method1_pytorch": method1_pytorch(tensor)}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
