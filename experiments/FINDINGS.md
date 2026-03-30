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
pipeline. We initially hypothesized from the nsys inter-kernel gaps that
method 2 was host-bottlenecked and method 4 was GPU-bottlenecked. However,
a simpler experiment disproved this (see Correction below).

**Inter-kernel gaps on GPU (from nsys, with original scalar kernel):**

| | Avg gap between consecutive GPU kernels |
|-|----------------------------------------|
| Method 2 | **20.6 us** |
| Method 4 | **7.7 us** |

**Inter-launch gaps on host (start-to-start):**

| | Avg time between consecutive `cudaLaunchKernel` starts |
|-|-------------------------------------------------------|
| Method 2 | **9.9 us** |
| Method 4 | **16.7 us** |

### Correction: Both Methods Are Kernel-Bottlenecked

The pipeline analysis above was **misleading**. Commenting out the kernel
launch in method 4 (after optimization) gives a definitive answer:

| Method | Description | Time (ms) |
|--------|------------|-----------|
| 4 | Full (optimized kernel) | 2.33 |
| 4 (no launch) | `<<<>>>` commented out | **0.25** |

Method 4's host-only path takes just 0.25 ms for 300 ops. The kernel
launch + GPU execution adds the remaining 2.08 ms — that's **89%** of
the wall-clock time. The host is clearly *not* the bottleneck.

The same applies to method 2: its host dispatch overhead is a small
fraction of the 2.03 ms wall clock. The 20 us inter-kernel gap on the
GPU does not mean the GPU is starved — it means the launch queue buffers
submissions and the wall clock is still dominated by total GPU execution
time across all 300 kernels.

**Both methods are kernel-bottlenecked.** The ~0.3 ms wall-clock difference
between method 2 (2.03 ms) and method 4 (2.33 ms) after kernel optimization
comes from method 4's extra host overhead (alloc/free/dispatch per op),
which adds latency between kernel submissions and slightly increases
inter-kernel GPU gaps.

### Root Cause (of original 3.1x gap)

The 2.8x GPU kernel execution time difference (21.4 us vs 7.6 us) comes from:

1. **No vectorized memory access.** Method 4's kernel loads/stores one `float`
   per thread. LibTorch's kernel uses `float4` (128-bit) loads/stores, achieving
   4x better memory throughput per transaction.
2. **4x more thread blocks.** 37,890 vs 9,473 blocks. More blocks means more
   scheduling overhead on the GPU and less work per thread.

## Summary (Before Optimization)

| | Method 2 | Method 4 |
|-|----------|----------|
| Host dispatch (300 ops) | ~included | ~0.25 ms |
| GPU kernel per op | 7.6 us | 21.4 us |
| Bottleneck | **Kernel** | **Kernel** |
| Wall clock (300 ops) | ~2.1 ms | ~6.5 ms |

## What We Know

1. **The gap is NOT in allocation/deallocation.** (Experiment 1)
2. **The gap is NOT from CUDA stream mismatch.** (Experiment 2)
3. **The gap is NOT in reshape.** (Experiment 3)
4. **The gap is NOT in per-invocation overhead.** (Experiment 4)
5. **The gap IS GPU kernel execution time.** Method 4's scalar kernel takes
   21.4 us vs LibTorch's vectorized kernel at 7.6 us. (Experiments 5 & 6)
6. **Both methods are kernel-bottlenecked.** Method 4's host-only path takes
   just 0.25 ms for 300 ops; the kernel launch + GPU execution dominates.
7. **Vectorizing the kernel closes the GPU kernel gap.** float4 loads +
   halved grid + int32 indexing + unroll brings method 4's kernel to within
   ~1.6% of LibTorch's (7,756 ns vs 7,635 ns).
8. **The remaining 0.3 ms wall-clock gap is host overhead.** Method 4's
   alloc/free/dispatch adds inter-kernel latency that stretches total GPU time.

## Resolution: Vectorized Kernel

Branch: `perf/vectorized-kernel`

Three changes to `common/csrc/add_kernel.cu` closed the GPU kernel time gap:

1. **Vectorized memory access.** Replaced scalar per-thread loads with `float4`
   (128-bit) loads/stores and a grid-stride loop, matching LibTorch's
   `vectorized_elementwise_kernel<4>` pattern.
2. **Halved grid size.** Sized the grid so each thread processes at least 2
   `float4` loads (8 elements), matching LibTorch's grid sizing. This halved
   the block count from 18,945 to 9,473.
3. **32-bit indexing + unroll hint.** Switched loop indices from `int64_t` to
   `int` and added `#pragma unroll 2` to match LibTorch's codegen quality.

### Progression (nsys GPU kernel time, wall clock)

| Version | Grid | GPU kernel (ns) | Wall clock (ms) |
|---------|------|-----------------|-----------------|
| Scalar (original) | 37,890 x 256 | 21,403 | 6.5 |
| + float4 vectorization | 18,945 x 128 | 11,623 | 3.6 |
| + halved grid (2 iters/thread) | 9,473 x 128 | 8,239 | 2.1 |
| + int32 indexing + unroll | 9,473 x 128 | 7,756 | 2.33 |
| LibTorch (reference) | 9,473 x 128 | 7,635 | 2.03 |

GPU kernel times now match within ~1.6% (7,756 ns vs 7,635 ns).

### Final All-Methods Benchmark

| Method | Description | Time (ms) |
|--------|------------|-----------|
| 1 | PyTorch Python API | 2.59 |
| 2 | LibTorch C++ (nanobind) | **2.03** |
| 3 | Python emulation | 4.16 |
| 4 | Custom kernel (nanobind) | **2.33** |
| 4 (no launch) | `<<<>>>` commented out | 0.25 |
| 5 | Numba JIT | 2.34 |

The remaining 0.3 ms gap between method 2 (2.03 ms) and method 4 (2.33 ms) is
host-side overhead: method 4 spends 0.25 ms on alloc/free/dispatch (vs
LibTorch's integrated path), which adds latency between kernel submissions
and stretches the total GPU execution time.
