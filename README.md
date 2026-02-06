# numba-eval

Benchmark CPU overhead for repeated PyTorch add/reshape chains on a CUDA tensor.

## Repo Layout

- `common/`: shared Python package (`numba_eval`) with timing utilities and shared CUDA kernel sources.
- `method1/`: PyTorch Python baseline.
- `method2/`: LibTorch C++ baseline.
- `method3/`: Python emulation with explicit checks (uses common CUDA kernel).
- `method4/`: C++ emulation with explicit checks (uses common CUDA kernel).
- `method5/`: C/CUDA bridge (Numba-compatible) + Python harness.

## Build the shared CUDA kernel (common.so)

```bash
./common/build_common.sh
```

## UV Setup

```bash
uv venv
uv pip install -e .
uv pip install "numba-eval[numba]"  # optional for method5a
```

## Python Benchmarks (Method 1/3/5)

```bash
# Method 1 (PyTorch Python)
uv run python method1/run.py --device cuda

# Method 3 (Python emulation)
uv run python method3/run.py --device cuda

# Method 5 (C/CUDA bridge)
uv run python method5/build_bridge.py
export NUMBA_EVAL_BRIDGE=$(uv run python -c "import method5.build_bridge as b; print(b.build_bridge())")
uv run python method5/run.py --device cuda
```

## C++ Benchmarks (Method 2/4)

```bash
# Method 2 (LibTorch)
export Torch_DIR=/path/to/libtorch/share/cmake/Torch
mkdir -p method2/build
cd method2/build
cmake ..
cmake --build . -j
./method2_libtorch

# Method 4 (custom emulation)
cd ../../method4
mkdir -p build
cd build
cmake ..
cmake --build . -j
./method4_custom
```

## Notes

- The timing is **CPU-only** and does **not** include `cudaDeviceSynchronize`.
- Method 3/4 intentionally keep all checks explicit and unoptimized to emulate compiler-generated code.
- Method 5 uses a CUDA kernel with a C ABI to keep it compatible with Numba's `cfunc` calling convention.
