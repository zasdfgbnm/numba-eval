# Method 2 vs Method 4 Performance Gap Investigation

## Problem

Method 2 (LibTorch `at::Tensor::add()` via nanobind) runs a chain of 300
add operations in **~2.1 ms**, while method 4 (custom CUDA kernel dispatched
through `dlopen`ed C functions `allocate_buf`/`add`/`free_buf`) takes
**~6.5 ms** — a **3.1x gap**.

Both methods perform the same computation (300 sequential float additions on a
CUDA tensor) and use PyTorch's caching allocator for memory. The question is:
where does the extra ~4.4 ms come from?

## Experiment 1: Allocation Strategy Sweep

**Hypothesis:** The overhead is in `allocate_buf`/`free_buf` — constructing
`at::Tensor` objects and maintaining an `unordered_map<ptr, Tensor>` to prevent
deallocation is expensive per-call.

**Approach:** We implemented 4 compile-time allocation strategies in
`common/csrc/allocate.cpp` and benchmarked each:

| Strategy | Description | Time (ms) |
|----------|-------------|-----------|
| 0 (baseline) | `at::empty` + `unordered_map<ptr, Tensor>` | 6.492 |
| 1 | `raw_alloc`/`raw_delete` only (no Tensor, no map) | 6.485 |
| 2 | `at::empty` + destroy + `raw_alloc` (Tensor cost, no map) | 6.491 |
| 3 | `raw_alloc` + `map<ptr, uint64_t>` (map cost, no Tensor) | 6.486 |

**Result:** All 4 strategies produce identical timings within noise (~6.49 ms).
The `at::Tensor` construction/destruction and the `unordered_map` bookkeeping
contribute **zero measurable overhead**.

**Script:** `experiments/run_alloc_experiment.sh`

## Experiment 2: CUDA Stream Mismatch Fix

**Hypothesis:** The caching allocator records allocations on PyTorch's current
CUDA stream (`cudaStreamLegacy`, value `0x1`), but `add_kernel.cu` launches
with `<<<blocks, threads>>>` (no stream argument), which targets `cudaStream_t(0)`.
If the allocator compares stream values numerically rather than semantically,
it would insert `cudaEvent` synchronizations before reusing freed blocks —
adding implicit sync overhead on every allocation.

**Approach:** Modified `common/csrc/add_kernel.cu` to explicitly launch on
`at::cuda::getCurrentCUDAStream()`:

```cuda
// Before
add_kernel<<<blocks, threads>>>(input, output, numel, alpha);

// After
cudaStream_t stream = at::cuda::getCurrentCUDAStream().stream();
add_kernel<<<blocks, threads, 0, stream>>>(input, output, numel, alpha);
```

**Result:**

| Method | Before fix | After fix |
|--------|-----------|-----------|
| Method 2 (LibTorch) | ~2.1 ms | ~2.1 ms |
| Method 4 (custom) | ~6.5 ms | ~6.5 ms |

No change. The stream mismatch was **not** causing allocator sync overhead on
this system. The fix is still correct practice (avoids potential issues in
multi-stream scenarios) and was merged, but it does not explain the gap.

## What We Know

1. **The gap is NOT in allocation/deallocation.** Stripping method 4's allocator
   down to bare `raw_alloc`/`raw_delete` (no Tensor, no map) has zero effect.
2. **The gap is NOT from CUDA stream mismatch.** Launching on the correct
   PyTorch stream has zero effect.
3. **The gap is consistent across all strategies (~6.49 ms)**, suggesting the
   bottleneck is in the per-operation dispatch path itself — the overhead of
   300 calls through `dlopen`ed C function pointers, Python→C transitions, or
   some other fixed cost that LibTorch's `at::Tensor::add()` avoids through
   its more integrated dispatch.

## Open Questions

- Is the overhead in the Python→C boundary (300 nanobind calls vs LibTorch's
  internal C++ loop)?
- Does LibTorch batch or fuse operations that method 4 executes individually?
- Is there CUDA launch overhead from 300 separate `<<<>>>` launches that
  LibTorch's `at::add` somehow amortizes?
- Could `nsys` profiling reveal where the extra time is spent?
