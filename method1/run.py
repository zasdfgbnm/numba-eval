import argparse
import json

import torch

from numba_eval.benchmark import time_cpu
from numba_eval.constants import LOOPS, SHAPE_A, SHAPE_B


def method1_pytorch(tensor: torch.Tensor) -> float:
    def op() -> None:
        out = tensor
        for _ in range(LOOPS):
            out = out.add(1)
            out = out.reshape(*SHAPE_A)
            out = out.add(-1)
            out = out.reshape(*SHAPE_B)
            out = out.add(0)

    return time_cpu(op, 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device)
    tensor = torch.empty(SHAPE_B, device=device, dtype=torch.float32)
    result = {"method1_pytorch": method1_pytorch(tensor)}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
