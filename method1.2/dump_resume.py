"""Capture Dynamo-generated resume-function bytecode for method1.2.

Run:  python method1.2/dump_resume.py --device cuda
Writes: method1.2/generated/resume_bytecode.py
"""

import argparse
import dis
import io
import os
import types

import torch
from torch._dynamo.convert_frame import register_bytecode_hook

GENERATED_DIR = os.path.join(os.path.dirname(__file__), "generated")
os.makedirs(GENERATED_DIR, exist_ok=True)

# Collect all bytecode transformations (original → modified) in order.
_records: list[str] = []


def _hook(code: types.CodeType, new_code: types.CodeType) -> None:
    buf = io.StringIO()
    buf.write(f"# === {new_code.co_name} ===\n")
    buf.write(f"# file: {new_code.co_filename}  firstlineno: {new_code.co_firstlineno}\n")
    buf.write(f"# argcount: {new_code.co_argcount}  varnames: {new_code.co_varnames[:new_code.co_argcount]}\n")
    buf.write(f"#\n# MODIFIED BYTECODE\n")
    buf.write(dis.Bytecode(new_code).dis())
    buf.write("\n")
    _records.append(buf.getvalue())
    return None  # do not replace code


handle = register_bytecode_hook(_hook)

# ---- build the same compiled function as run.py ----

_lines = ["def _method1_2_inner(tensor):"]
_lines.append("    out = tensor")
for _i in range(100):
    _lines.append("    out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)")
    _lines.append("    out = out.add(0)")
    _lines.append("    out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)")
    _lines.append("    torch._dynamo.graph_break()")
_lines.append("    return out")
exec(compile("\n".join(_lines), "method1.2/run.py", "exec"))

method1_2_compiled = torch.compile(_method1_2_inner)  # type: ignore[name-defined]

# ---- invoke once to trigger compilation of all graphs + resume fns ----

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    device = torch.device(args.device)
    tensor = torch.empty(
        (2, 3, 5, 7, 11, 13, 17, 19), device=device, dtype=torch.float32
    )
    method1_2_compiled(tensor)

    handle.remove()

    outfile = os.path.join(GENERATED_DIR, "resume_bytecode.py")
    with open(outfile, "w") as f:
        f.write(f"# Auto-generated Dynamo resume-function bytecode for method1.2\n")
        f.write(f"# {len(_records)} compiled frame(s) captured\n\n")
        for record in _records:
            f.write(record)
            f.write("\n")

    print(f"Wrote {len(_records)} frame(s) to {outfile}")
