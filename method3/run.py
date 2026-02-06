import argparse
import json
from typing import Sequence

import torch

from numba_eval.benchmark import time_cpu
from op_add import launch_add
from op_reshape import reshape_with_checks


SHAPE_A = (19, 17, 13, 11, 7, 5, 3, 2)
SHAPE_B = (2, 3, 5, 7, 11, 13, 17, 19)
LOOPS = 100


def emulate_add_reshape_chain(
    tensor: torch.Tensor,
    shape_a: Sequence[int],
    shape_b: Sequence[int],
) -> torch.Tensor:
    flat = tensor.reshape(-1)
    shape: tuple[int, ...] = (flat.numel(),)
    stride: tuple[int, ...] = (1,)

    flat = launch_add(flat, 1.0)
    shape, stride = reshape_with_checks(shape, stride, shape_a)
    flat = launch_add(flat, -1.0)
    shape, stride = reshape_with_checks(shape, stride, shape_b)
    flat = launch_add(flat, 0.0)

    output = torch.empty_strided(
        shape_b,
        stride,
        device=tensor.device,
        dtype=tensor.dtype,
    )
    output.view(-1).copy_(flat)
    return output


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

    tensor = torch.empty(SHAPE_B, device=device, dtype=torch.float32)
    result = {"method3_python_emulation": method3_python_emulation(tensor)}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
