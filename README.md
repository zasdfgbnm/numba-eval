# numba-eval

Benchmark CPU overhead for repeated PyTorch add/reshape chains on a CUDA tensor.

## Repo Layout

- `common/`: shared Python modules (on `PYTHONPATH`) + shared CUDA kernel sources.
- `method1/`: PyTorch Python baseline.
- `method1.1/`: PyTorch + `torch.compile` (full graph, fused to 1 kernel).
- `method1.2/`: PyTorch + `torch.compile` (per-iteration graph break).
- `method2/`: LibTorch C++ baseline.
- `method3/`: Python emulation with explicit checks (uses common CUDA kernel).
- `method4/`: C++ emulation with explicit checks (uses common CUDA kernel).
- `method5/`: C/CUDA bridge (Numba-compatible) + Python harness.

## Build the shared common library (`libcommon`)

You normally don't need to run this manually: `run_cpu.sh` / `run_gpu.sh` will
build it via CMake automatically.

If you want to build it directly:

```bash
# CPU
cmake -S common -B common/build_cpu -DCMAKE_BUILD_TYPE=Release -DNUMBA_EVAL_USE_CUDA=OFF
cmake --build common/build_cpu -j

# CUDA (requires nvcc + CUDA toolkit)
cmake -S common -B common/build_cuda -DCMAKE_BUILD_TYPE=Release -DNUMBA_EVAL_USE_CUDA=ON
cmake --build common/build_cuda -j
```

## UV Setup

```bash
uv venv
uv pip install -e .
```

## Python Benchmarks (Method 1/1.1/1.2/3/5)

```bash
# Method 1 (PyTorch Python)
uv run python method1/run.py --device cuda

# Method 1.1 (PyTorch + torch.compile, fused)
uv run python method1.1/run.py --device cuda

# Method 1.2 (PyTorch + torch.compile, per-step)
uv run python method1.2/run.py --device cuda

# Method 2 (LibTorch C++ via nanobind)
# (Build the bindings first; see below.)
uv run python method2/run.py --device cuda

# Method 3 (Python emulation)
uv run python method3/run.py --device cuda

# Method 4 (custom emulation C++ via nanobind)
# (Build the bindings first; see below.)
uv run python method4/run.py --device cuda

# Method 5 (method3 + Numba JIT)
uv run python method5/run.py --device cuda
```

## Build Python bindings (nanobind) for Method 2/4

This builds two Python extension modules into `common/`:
- `method2_api` (LibTorch baseline)
- `method4_api` (custom emulation)

```bash
TORCH_PREFIX="$(uv run python -c 'import torch; print(torch.utils.cmake_prefix_path)')"
# Use a Python that has development headers (Python.h). On macOS, Homebrew's
# python@3.12 works well even if you run benchmarks via `uv run`.
PYTHON_HEADERS_BIN="$(python3.12 -c 'import sys; print(sys.executable)')"
cmake -S bindings -B bindings/build \
  -DCMAKE_BUILD_TYPE=Release \
  -DPython_EXECUTABLE="$PYTHON_HEADERS_BIN" \
  -DCMAKE_PREFIX_PATH="$TORCH_PREFIX"
cmake --build bindings/build -j
```

## Notes

- The timing is **CPU-only** and does **not** include `cudaDeviceSynchronize`.
- Method 3/4 intentionally keep all checks explicit and unoptimized to emulate compiler-generated code.
- Method 5 uses the same C ABI (`libcommon`) and can optionally JIT the chain with Numba.

## Benchmark Results

Measured on 4x NVIDIA GB200 (sm_100), CUDA 13.2, aarch64 Linux.
Each iteration runs reshape-add(0)-reshape (100 iterations, 100 kernel launches).

| Method | Description | Time (ms) |
|--------|------------|-----------|
| 1 | PyTorch Python API | 1.08 |
| 1.1 | `torch.compile` (fused, 1 kernel) | 0.04 |
| 1.2 | `torch.compile` (per-iteration graph break) | 1.44 |
| 2 | LibTorch C++ (nanobind) | 0.90 |
| 3 | Python emulation | 2.76 |
| 4 | Custom kernel (nanobind) | 0.28 |
| 5 | Numba JIT | 0.28 |

Methods 4 and 5 are fastest because their lean host dispatch paths (~3 us/op)
outweigh LibTorch's heavier dispatch (~10 us/op) when GPU kernels are cheap.
See `experiments/FINDINGS.md` for detailed profiling and analysis.
