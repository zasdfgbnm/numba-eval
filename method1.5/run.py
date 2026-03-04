import argparse
import json

import torch

from benchmark import time_cpu  # type: ignore[import-not-found]


def _method1_5_inner(tensor: torch.Tensor) -> None:
    out = tensor
    for _ in range(100):
        out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out = out.add(0)
        out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)


method1_5_compiled = torch.compile(_method1_5_inner)


def method1_5(tensor: torch.Tensor) -> None:
    method1_5_compiled(tensor)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device)
    tensor = torch.empty((2, 3, 5, 7, 11, 13, 17, 19), device=device, dtype=torch.float32)

    def op() -> None:
        method1_5(tensor)

    seconds = time_cpu(op, 1)

    result = {"method1.5_ms": seconds}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
