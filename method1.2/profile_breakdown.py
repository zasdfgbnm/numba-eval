"""Profile the CPU-time breakdown of one method1_2_compiled() call.

Patches:
  - CompiledFxGraph.__call__  →  Inductor code (Runner.call + Triton kernel launch)
  - SerializableCompiledFunction.__call__  →  full compiled-fn path (AOT + Inductor)
  - Difference  →  AOT Autograd wrapper overhead
  - Remainder  →  Dynamo overhead (C++ guards, eval_frame hook, resume functions)
"""

import argparse
import json
import time

import torch


# ---------------------------------------------------------------------------
# Build the same function as run.py
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
# Accumulators
# ---------------------------------------------------------------------------
inductor_ns = 0
compiled_fn_ns = 0

# ---------------------------------------------------------------------------
# Patch CompiledFxGraph.__call__  (innermost: Runner.call + kernel)
# ---------------------------------------------------------------------------
import torch._inductor.output_code as _oc_mod  # noqa: E402

_orig_inductor_call = _oc_mod.CompiledFxGraph.__call__


def _timed_inductor_call(self, inputs):  # type: ignore[no-untyped-def]
    global inductor_ns
    t0 = time.perf_counter_ns()
    result = _orig_inductor_call(self, inputs)
    inductor_ns += time.perf_counter_ns() - t0
    return result


_oc_mod.CompiledFxGraph.__call__ = _timed_inductor_call

# ---------------------------------------------------------------------------
# Patch SerializableCompiledFunction.__call__  (AOT wrapper → Inductor)
# ---------------------------------------------------------------------------
import torch._functorch._aot_autograd.runtime_wrappers as _rw_mod  # noqa: E402

_orig_scf_call = _rw_mod.SerializableCompiledFunction.__call__


def _timed_scf_call(self, *args, **kwargs):  # type: ignore[no-untyped-def]
    global compiled_fn_ns
    t0 = time.perf_counter_ns()
    result = _orig_scf_call(self, *args, **kwargs)
    compiled_fn_ns += time.perf_counter_ns() - t0
    return result


_rw_mod.SerializableCompiledFunction.__call__ = _timed_scf_call


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    global inductor_ns, compiled_fn_ns

    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--iterations", type=int, default=200)
    args = parser.parse_args()

    device = torch.device(args.device)
    tensor = torch.empty(
        (2, 3, 5, 7, 11, 13, 17, 19), device=device, dtype=torch.float32
    )

    # Warmup
    method1_2_compiled(tensor)

    # Measure
    torch.cuda.synchronize()
    total_ns = 0
    inductor_ns = 0
    compiled_fn_ns = 0

    for _ in range(args.iterations):
        torch.cuda.synchronize()
        t0 = time.perf_counter_ns()
        method1_2_compiled(tensor)
        torch.cuda.synchronize()
        total_ns += time.perf_counter_ns() - t0

    n = args.iterations
    total_ms = total_ns / 1e6
    inductor_ms = inductor_ns / 1e6
    compiled_fn_ms = compiled_fn_ns / 1e6
    aot_ms = compiled_fn_ms - inductor_ms
    dynamo_ms = total_ms - compiled_fn_ms

    print(f"Iterations: {n}  |  Per-call: {total_ms/n:.3f} ms\n")
    print(f"{'Component':<40} {'Total ms':>10} {'Per-call ms':>12} {'%':>7}")
    print("=" * 72)
    print(f"{'Dynamo (guards + eval_frame + resume)':<40} {dynamo_ms:>10.2f} {dynamo_ms/n:>12.4f} {dynamo_ms/total_ms*100:>6.1f}%")
    print(f"{'AOT Autograd wrappers':<40} {aot_ms:>10.2f} {aot_ms/n:>12.4f} {aot_ms/total_ms*100:>6.1f}%")
    print(f"{'Inductor (Runner.call + kernel launch)':<40} {inductor_ms:>10.2f} {inductor_ms/n:>12.4f} {inductor_ms/total_ms*100:>6.1f}%")
    print("=" * 72)
    print(f"{'TOTAL':<40} {total_ms:>10.2f} {total_ms/n:>12.4f} {'100.0':>6}%")

    print("\n" + json.dumps({
        "iterations": n,
        "per_call_ms": round(total_ms / n, 4),
        "total_ms": round(total_ms, 2),
        "dynamo_pct": round(dynamo_ms / total_ms * 100, 1),
        "aot_pct": round(aot_ms / total_ms * 100, 1),
        "inductor_pct": round(inductor_ms / total_ms * 100, 1),
    }, indent=2))


if __name__ == "__main__":
    main()
