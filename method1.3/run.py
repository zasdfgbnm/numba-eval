import argparse
import json

import torch

from benchmark import time_cpu  # type: ignore[import-not-found]


# Manually unroll the loop so that graph_break() is in straight-line code
# (Dynamo does not support graph_break inside a for/while loop).
_lines = ["def _method1_3_inner(tensor):"]
_lines.append("    out = tensor")
for _i in range(100):
    _lines.append("    out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)")
    _lines.append("    out = out.add(0)")
    _lines.append("    out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)")
    _lines.append("    torch._dynamo.graph_break()")
_lines.append("    return out")
exec(compile("\n".join(_lines), __file__, "exec"))

method1_3_compiled = torch.compile(_method1_3_inner)  # type: ignore[name-defined]


def method1_3(tensor: torch.Tensor) -> torch.Tensor:
    return method1_3_compiled(tensor)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device)
    tensor = torch.empty((2, 3, 5, 7, 11, 13, 17, 19), device=device, dtype=torch.float32)

    def op() -> None:
        method1_3(tensor)

    seconds = time_cpu(op, 1)

    result = {"method1.3_ms": seconds}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
