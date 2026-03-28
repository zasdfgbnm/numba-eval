# Method 1.2: `torch.compile` + `graph_break()` (100 subgraphs)

Manually unrolls 100 reshape-add-reshape iterations with `torch._dynamo.graph_break()`
between each one. Dynamo traces each iteration as a separate subgraph; Inductor compiles
each into a standalone Triton kernel.

## CPU-time breakdown

Measured on GB200 (sm_100), CUDA 13.2, aarch64 Linux. 200 iterations, `cuda.synchronize()`
between each call. Per-call average: **~5.5 ms**.

| Component | % | Per-call | What it covers |
|---|---|---|---|
| Inductor (Runner.call + kernel launch) | ~52% | ~2.9 ms | 100x `Runner.call` → buffer alloc, `assert_size_stride`, Triton kernel launch, `reinterpret_tensor` |
| Dynamo (guards + eval_frame + resume fns) | ~31% | ~1.7 ms | 100x C++ guard checks (`run_root_guard_manager`) + eval_frame hook + resume function chain |
| AOT Autograd wrappers | ~17% | ~0.9 ms | 100x `SerializableCompiledFunction` → `runtime_wrapper` → `wrapper` Python dispatch |
| **Total** | **100%** | **~5.5 ms** | |

### How it works

Each `graph_break()` forces Dynamo to:
1. End the current FX graph
2. Compile it via Inductor into a standalone Triton kernel + `Runner.call`
3. Generate a **resume function** (`torch_dynamo_resume_in__method1_2_inner_at_N`)
   that re-enters the next iteration through the eval_frame hook

At steady state (after first call), each of the 100 subgraphs goes through:
```
eval_frame C hook
  → C++ guard check (run_root_guard_manager)
  → resume function bytecode
  → AOT Autograd (SerializableCompiledFunction → runtime_wrapper → wrapper)
  → Inductor (CompiledFxGraph.__call__ → Runner.call → triton kernel launch)
```

The resume functions form a deeply nested call chain (100 levels), visible as a
staircase pattern in the flamegraph.

### Why each subgraph = exactly 1 Triton kernel

Inductor cannot see across graph breaks. Each subgraph captures:
```python
out   = tensor.reshape(19, 17, 13, 11, 7, 5, 3, 2)   # view (stride change only)
out_1 = out.add(0)                                      # pointwise add
out_2 = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19)     # view (stride change only)
```
Inductor fuses this into one kernel: `triton_poi_fused_add_view_0`. The reshapes become
`reinterpret_tensor` (zero-cost stride manipulation); only the `add(0)` copies data.

Result: **100 graph breaks → 100 separate Inductor modules → 100 Triton kernel launches**.

## Generated artifacts

| File | Description |
|---|---|
| `generated/dynamo_graph.py` | FX graphs traced by Dynamo (100 identical subgraphs) |
| `generated/guards.py` | Guard conditions checked before using cached compiled code |
| `generated/resume_bytecode.py` | Resume function bytecode (one per `graph_break`) |
| `generated/inductor_output_code.py` | Inductor output: 100x Triton kernel + Runner class (12K lines) |
| `generated/flamegraph.svg` | py-spy flamegraph of steady-state execution |

## Profiling scripts

```bash
# CPU-time breakdown table
python method1.2/profile_breakdown.py --device cuda

# Generate py-spy flamegraph
py-spy record -o method1.2/generated/flamegraph.svg -- python method1.2/profile_flamegraph.py --device cuda
```
