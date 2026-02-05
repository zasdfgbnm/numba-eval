import argparse
import json

import torch

from numba_eval.benchmark import time_cpu
from numba_eval.constants import LOOPS, SHAPE_A, SHAPE_B
from ops_emulation import emulate_add_reshape_chain


def method3_python_emulation(tensor: torch.Tensor) -> float:
    def op() -> None:
        _ = emulate_add_reshape_chain(tensor, SHAPE_A, SHAPE_B)

    return time_cpu(op, LOOPS)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device)
    tensor = torch.empty(SHAPE_B, device=device, dtype=torch.float32)
    result = {"method3_python_emulation": method3_python_emulation(tensor)}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
