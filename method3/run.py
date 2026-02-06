import argparse
import json

import torch

from numba_eval.benchmark import time_cpu
from ops_emulation import emulate_add_reshape_chain


SHAPE_A = (19, 17, 13, 11, 7, 5, 3, 2)
SHAPE_B = (2, 3, 5, 7, 11, 13, 17, 19)
LOOPS = 100


def method3_python_emulation(tensor: torch.Tensor) -> float:
    def op() -> None:
        out = tensor
        for _ in range(LOOPS):
            out = emulate_add_reshape_chain(out, SHAPE_A, SHAPE_B)

    return time_cpu(op, 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device)
    if device.type != "cuda":
        print(json.dumps({"method3_error": "method3 requires CUDA for common kernel"}, indent=2))
        return

    tensor = torch.empty(SHAPE_B, device=device, dtype=torch.float32)
    result = {"method3_python_emulation": method3_python_emulation(tensor)}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
