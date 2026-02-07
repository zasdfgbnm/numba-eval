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

## Experiment 3: Reshape Removal

**Hypothesis:** The `reshape` calls (2 per iteration, 200 total) add overhead
in method 4's C++ `compute_view_stride` logic that LibTorch avoids.

**Approach:** Removed both `reshape` calls from the loop body in both
`method2/chain.cpp` and `method4/chain.cpp`, leaving only the 3 `add`
operations per iteration.

**Result:**

| Method | With reshape | Without reshape |
|--------|-------------|-----------------|
| Method 2 (LibTorch) | ~2.09 ms | ~2.12 ms |
| Method 4 (custom) | ~6.49 ms | ~6.50 ms |

No change. Reshape is pure metadata manipulation (view on contiguous tensor)
in both methods and costs essentially nothing.

## Experiment 4: No-Op Chain

**Hypothesis:** The overhead could be in the Python→C boundary, `dlopen`
function-pointer setup, or other per-invocation fixed cost outside the loop.

**Approach:** Made both chains no-ops — the function is called but the 100-
iteration loop body is entirely removed.

**Result:**

| Method | Full chain | No-op |
|--------|-----------|-------|
| Method 2 (LibTorch) | ~2.09 ms | ~0.0015 ms |
| Method 4 (custom) | ~6.49 ms | ~0.012 ms |

Both drop to near-zero. The Python→C call, `dlopen`, and per-invocation setup
are negligible. **The entire gap is inside the 300 kernel dispatches.**

## What We Know

1. **The gap is NOT in allocation/deallocation.** Stripping method 4's allocator
   down to bare `raw_alloc`/`raw_delete` (no Tensor, no map) has zero effect.
2. **The gap is NOT from CUDA stream mismatch.** Launching on the correct
   PyTorch stream has zero effect.
3. **The gap is NOT in reshape.** Removing reshapes has zero effect.
4. **The gap is NOT in per-invocation overhead.** No-op chains are near-zero
   for both methods.
5. **The gap is entirely in the 300 per-iteration kernel dispatches.** Something
   method 4 does differently *per kernel launch* compared to LibTorch's
   `at::Tensor::add()` accounts for the full ~4.4 ms difference.

## Open Questions

- What does LibTorch's `at::add` dispatch path do differently per-launch that
  makes it ~3x faster than a raw `<<<>>>` kernel launch + caching allocator
  alloc/free?
- Could `nsys` profiling reveal where the extra time is spent per-launch?
