import argparse
import json
import os
from typing import Tuple

import torch

from numba_eval.benchmark import time_cpu
from numba_eval.constants import LOOPS, SHAPE_B


def method5_bridge(tensor: torch.Tensor, use_numba: bool) -> Tuple[float, str]:
    import ctypes

    ext_path = os.environ.get("NUMBA_EVAL_BRIDGE")
    if not ext_path or not os.path.exists(ext_path):
        return float("nan"), "bridge library not found (set NUMBA_EVAL_BRIDGE)"

    bridge = ctypes.CDLL(ext_path)
    bridge.torch_cuda_empty.argtypes = [ctypes.c_int64]
    bridge.torch_cuda_empty.restype = ctypes.c_int64
    bridge.torch_cuda_data_ptr.argtypes = [ctypes.c_int64]
    bridge.torch_cuda_data_ptr.restype = ctypes.c_uint64
    bridge.torch_cuda_launch_add.argtypes = [ctypes.c_uint64, ctypes.c_uint64, ctypes.c_int64, ctypes.c_float]
    bridge.torch_cuda_launch_add.restype = None

    def op() -> None:
        handle = bridge.torch_cuda_empty(tensor.numel())
        out_ptr = bridge.torch_cuda_data_ptr(handle)
        in_ptr = tensor.data_ptr()
        bridge.torch_cuda_launch_add(in_ptr, out_ptr, tensor.numel(), 1.0)
        bridge.torch_cuda_launch_add(out_ptr, out_ptr, tensor.numel(), -1.0)
        bridge.torch_cuda_launch_add(out_ptr, out_ptr, tensor.numel(), 0.0)

    if use_numba:
        try:
            import numba  # noqa: F401
        except Exception as exc:  # pragma: no cover - environment dependent
            return float("nan"), f"numba unavailable: {exc}"

    return time_cpu(op, LOOPS), "ok"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device)
    if device.type != "cuda":
        print(json.dumps({"method5_error": "method5 requires CUDA"}, indent=2))
        return

    tensor = torch.empty(SHAPE_B, device=device, dtype=torch.float32)

    results = {}
    time5a, note5a = method5_bridge(tensor, use_numba=True)
    results["method5a_bridge_numba"] = time5a
    results["method5a_note"] = note5a

    time5b, note5b = method5_bridge(tensor, use_numba=False)
    results["method5b_bridge_python"] = time5b
    results["method5b_note"] = note5b

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
