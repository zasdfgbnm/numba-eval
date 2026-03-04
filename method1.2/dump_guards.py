"""Capture Dynamo-generated guard code for method1.2.

Run:  python method1.2/dump_guards.py --device cuda
Writes: method1.2/generated/guards.py
"""

import argparse
import io
import os
import types

import torch
from torch._dynamo.convert_frame import register_bytecode_hook
from torch._dynamo.eval_frame import _debug_get_cache_entry_list

GENERATED_DIR = os.path.join(os.path.dirname(__file__), "generated")
os.makedirs(GENERATED_DIR, exist_ok=True)

# Collect (original_code, modified_code) pairs in compilation order.
_code_pairs: list[tuple[types.CodeType, types.CodeType]] = []


def _hook(code: types.CodeType, new_code: types.CodeType) -> None:
    _code_pairs.append((code, new_code))
    return None


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

    # ---- dump guards for every compiled frame ----

    buf = io.StringIO()
    buf.write("# Auto-generated Dynamo guard conditions for method1.2\n")
    buf.write(f"# {len(_code_pairs)} compiled frame(s)\n\n")

    for i, (orig_code, mod_code) in enumerate(_code_pairs):
        buf.write(f"# === Frame {i}: {mod_code.co_name} ===\n")
        buf.write(f"# file: {mod_code.co_filename}  firstlineno: {mod_code.co_firstlineno}\n")

        # Cache entries are keyed on the *original* code object.
        entries = _debug_get_cache_entry_list(orig_code)
        if not entries:
            buf.write("# (no cache entries found)\n\n")
            continue

        for j, entry in enumerate(entries):
            gm = entry.guard_manager
            buf.write(f"#\n# CacheEntry {j}, compile_id={entry.compile_id}\n")
            buf.write(f"# Guard tree:\n")
            for line in str(gm).splitlines():
                buf.write(f"#   {line}\n")
            buf.write("#\n# Guard conditions (code_parts):\n")
            if hasattr(gm, "code_parts"):
                for part in gm.code_parts:
                    buf.write(f"#   {part}\n")
            buf.write("\n")

    outfile = os.path.join(GENERATED_DIR, "guards.py")
    with open(outfile, "w") as f:
        f.write(buf.getvalue())

    print(f"Wrote guards for {len(_code_pairs)} frame(s) to {outfile}")
