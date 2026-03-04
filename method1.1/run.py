import argparse
import json

import torch

from benchmark import time_cpu  # type: ignore[import-not-found]


def _method1_1_inner(tensor: torch.Tensor) -> torch.Tensor:
    out = tensor
    for _ in range(100):
        out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out = out.add(0)
        out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
    return out


method1_1_compiled = torch.compile(_method1_1_inner)


def method1_1(tensor: torch.Tensor) -> torch.Tensor:
    return method1_1_compiled(tensor)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device)
    tensor = torch.empty((2, 3, 5, 7, 11, 13, 17, 19), device=device, dtype=torch.float32)

    def op() -> None:
        method1_1(tensor)

    seconds = time_cpu(op, 1)

    result = {"method1.1_ms": seconds}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
