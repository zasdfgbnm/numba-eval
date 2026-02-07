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

## Experiment 5: Kernel Launch Removal

**Hypothesis:** The `<<<>>>` kernel launch itself is the dominant cost in
method 4.

**Approach:** Commented out the single `add_kernel<<<...>>>` line in
`common/csrc/add_kernel.cu`. The `add()` C function still computes `blocks`,
`threads`, and fetches the current CUDA stream — it just doesn't launch.
Method 2 is unchanged (LibTorch still launches its own kernels).

**Result:**

| Method | Full chain | No kernel launch |
|--------|-----------|-----------------|
| Method 2 (LibTorch) | ~2.02 ms | ~2.02 ms (unchanged) |
| Method 4 (custom) | ~6.49 ms | **~0.25 ms** |

Method 4 drops from ~6.5 ms to **0.25 ms**. The kernel launch accounts for
**~6.2 ms** of the 6.5 ms total (~96%). The remaining 0.25 ms is the cost of
300x alloc/free + reshape + C++ dispatch with no GPU work.

Note: without the kernel launch, `cudaLaunchKernel` never blocks (no GPU
back-pressure), so the 0.25 ms reflects pure host-side work. The full 6.5 ms
includes both GPU execution time and host stalls waiting for the GPU queue.

## Experiment 6: nsys Profiling

**Goal:** Understand exactly where the time goes — is it host-side launch
overhead or GPU kernel execution time?

**Approach:** Profiled both methods with `nsys profile --stats=true -t cuda`.

### CUDA API Summary (host-side)

| API Call | Method 2 Calls | Method 2 Avg (ns) | Method 4 Calls | Method 4 Avg (ns) |
|----------|---------------|-------------------|---------------|-------------------|
| `cudaLaunchKernel` | 4500 | 4,865 | 4500 | 13,154 |
| `cuKernelGetName` | 0 | — | 4500 | 60 |
| `cuGetProcAddress_v2` | 0 | — | 475 | 249 |
| `cuLibraryLoadData` | 0 | — | 1 | 74,240 |

Method 4's `cudaLaunchKernel` average is inflated to 13.2 us, but this is
**not** because the launch call itself is slow — it's because the call
**blocks** when the GPU launch queue is full (back-pressure from slow GPU
kernels). Method 4's `cudaLaunchKernel` call itself takes ~3 us, but the
call stalls waiting for the GPU to finish previous kernels.

### GPU Kernel Execution

| | Kernel | Grid | Block | Regs/Thread | Avg GPU Time (ns) |
|-|--------|------|-------|-------------|-------------------|
| Method 2 | `vectorized_elementwise_kernel<4, ...>` | 9,473 x 1 x 1 | 128 x 1 x 1 | 32 | **7,615** |
| Method 4 | `add_kernel` | 37,890 x 1 x 1 | 256 x 1 x 1 | 16 | **21,403** |

Tensor has 9,699,690 elements (`2*3*5*7*11*13*17*19`).

**Method 2 (LibTorch):** Uses `vectorized_elementwise_kernel<4>` which loads
`float4` (4 floats per memory transaction). 128 threads/block, each thread
processes ~8 elements (two `float4` loads with grid-stride loop). Only **9,473
blocks** needed.

**Method 4 (custom):** Scalar kernel — 1 float per thread, 256 threads/block.
Requires **37,890 blocks** (4x more) with scalar memory access.

### Pipeline Analysis: Who's the Bottleneck?

Since `cudaLaunchKernel` is asynchronous, the host and GPU operate as a
pipeline. The wall-clock time is determined by whichever stage is slower.

**Inter-kernel gaps on GPU:**

| | Avg gap between consecutive GPU kernels |
|-|----------------------------------------|
| Method 2 | **20.6 us** (GPU starved — idle between kernels) |
| Method 4 | **7.7 us** (GPU nearly saturated) |

**Inter-launch gaps on host (start-to-start):**

| | Avg time between consecutive `cudaLaunchKernel` starts |
|-|-------------------------------------------------------|
| Method 2 | **9.9 us** |
| Method 4 | **16.7 us** |

**Method 2 is host-bottlenecked.** Its GPU kernels finish in 7.6 us, but the
host takes ~9.9 us to dispatch the next one (LibTorch's C++ dispatch: tensor
metadata, allocator, op dispatch). The GPU sits idle for ~20 us between
kernels — it could go faster if the host dispatched faster.

**Method 4 is GPU-bottlenecked.** Its host dispatch is actually *faster* (~6 us
for alloc + C function pointer call + launch) but the GPU kernel takes 21.4 us.
The host submits faster than the GPU can execute, the launch queue fills up, and
`cudaLaunchKernel` stalls (blocking inside the call) until a slot opens. This
is why the measured `cudaLaunchKernel` duration averages 13.2 us despite the
actual submission taking only ~3 us.

### Root Cause

The 2.8x GPU kernel execution time difference (21.4 us vs 7.6 us) comes from:

1. **No vectorized memory access.** Method 4's kernel loads/stores one `float`
   per thread. LibTorch's kernel uses `float4` (128-bit) loads/stores, achieving
   4x better memory throughput per transaction.
2. **4x more thread blocks.** 37,890 vs 9,473 blocks. More blocks means more
   scheduling overhead on the GPU and less work per thread.

The GPU kernel quality difference causes method 4 to be GPU-bound, while
method 2 (with its fast kernel) is host-bound. The wall clock reflects
whichever bottleneck dominates: method 4's slow GPU kernel (6.5 ms) vs
method 2's host dispatch overhead (2.1 ms).

## Summary

| | Method 2 | Method 4 |
|-|----------|----------|
| Host dispatch per op | ~9.9 us | ~6 us |
| GPU kernel per op | 7.6 us | 21.4 us |
| Bottleneck | **Host** (dispatch) | **GPU** (kernel) |
| Wall clock (300 ops) | ~2.1 ms | ~6.5 ms |

Method 4's host-side dispatch is actually leaner than LibTorch's. But its
naive scalar GPU kernel is 2.8x slower. Since method 4 is GPU-bound, the
wall clock is dominated by GPU kernel time.

Ironically, method 2 has the opposite problem: its vectorized kernel is fast,
but the host can't feed it fast enough — the GPU sits idle 73% of the time
(20.6 us idle out of 28.2 us cycle). Improving method 2's host dispatch speed
would improve its wall clock time.

## What We Know

1. **The gap is NOT in allocation/deallocation.** (Experiment 1)
2. **The gap is NOT from CUDA stream mismatch.** (Experiment 2)
3. **The gap is NOT in reshape.** (Experiment 3)
4. **The gap is NOT in per-invocation overhead.** (Experiment 4)
5. **The gap IS GPU kernel execution time.** Method 4's scalar kernel takes
   21.4 us vs LibTorch's vectorized kernel at 7.6 us. (Experiments 5 & 6)
6. **Method 4's host dispatch is faster than LibTorch's** (~6 us vs ~9.9 us),
   but this doesn't help because the GPU is the bottleneck.

## Open Questions

- Would a vectorized `float4` kernel in method 4 match LibTorch's GPU
  kernel performance and close the wall-clock gap?
- If method 4's kernel were fast enough to make it host-bottlenecked (like
  method 2), would its leaner dispatch path make it *faster* than LibTorch?
