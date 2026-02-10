import argparse
import json

import torch

import method2_nb  # type: ignore[import-not-found]
from benchmark import time_cpu  # type: ignore[import-not-found]


SHAPE_B = (2, 3, 5, 7, 11, 13, 17, 19)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device)
    tensor = torch.empty(SHAPE_B, device=device, dtype=torch.float32)

    def op() -> None:
        method2_nb.run_chain(tensor)

    seconds = time_cpu(op, 1)
    result = {"method2_libtorch_nanobind_ms": seconds}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
