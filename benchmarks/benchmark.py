import argparse
import json
import os
import sys
import time
from typing import Callable, Dict, Tuple

import torch

sys.path.append(os.path.dirname(__file__))
from ops_emulation import emulate_add_reshape_chain


SHAPE_A = (19, 17, 13, 11, 7, 5, 3, 2)
SHAPE_B = (2, 3, 5, 7, 11, 13, 17, 19)
LOOPS = 100


def _time_cpu(fn: Callable[[], None], iters: int) -> float:
    start = time.perf_counter()
    for _ in range(iters):
        fn()
    end = time.perf_counter()
    return end - start


def method1_pytorch(tensor: torch.Tensor) -> float:
    def op():
        out = tensor.add(1)
        out = out.reshape(*SHAPE_A)
        out = out.add(-1)
        out = out.reshape(*SHAPE_B)
        _ = out.add(0)

    return _time_cpu(op, LOOPS)


def method3_python_emulation(tensor: torch.Tensor) -> float:
    def op():
        _ = emulate_add_reshape_chain(tensor, SHAPE_A, SHAPE_B)

    return _time_cpu(op, LOOPS)


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

    def op():
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

    return _time_cpu(op, LOOPS), "ok"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device)
    tensor = torch.empty(SHAPE_B, device=device, dtype=torch.float32)

    results: Dict[str, float] = {}

    results["method1_pytorch"] = method1_pytorch(tensor)
    results["method3_python_emulation"] = method3_python_emulation(tensor)

    time5a, note5a = method5_bridge(tensor, use_numba=True)
    results["method5a_bridge_numba"] = time5a
    results["method5a_note"] = note5a

    time5b, note5b = method5_bridge(tensor, use_numba=False)
    results["method5b_bridge_python"] = time5b
    results["method5b_note"] = note5b

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
