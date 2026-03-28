import argparse

import torch


# Manually unroll the loop so that graph_break() is in straight-line code
# (Dynamo does not support graph_break inside a for/while loop).
_lines = ["def _method1_2_inner(tensor):"]
_lines.append("    out = tensor")
for _i in range(100):
    _lines.append("    out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)")
    _lines.append("    out = out.add(0)")
    _lines.append("    out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)")
    _lines.append("    torch._dynamo.graph_break()")
_lines.append("    return out")
exec(compile("\n".join(_lines), __file__, "exec"))

method1_2_compiled = torch.compile(_method1_2_inner)  # type: ignore[name-defined]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--iterations", type=int, default=1000)
    args = parser.parse_args()

    device = torch.device(args.device)
    tensor = torch.empty(
        (2, 3, 5, 7, 11, 13, 17, 19), device=device, dtype=torch.float32
    )

    # Warmup: trigger compilation
    method1_2_compiled(tensor)

    # Steady-state loop for py-spy sampling
    for _ in range(args.iterations):
        method1_2_compiled(tensor)


if __name__ == "__main__":
    main()
