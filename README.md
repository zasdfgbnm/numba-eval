# numba-eval

Benchmark CPU overhead for repeated PyTorch add/reshape chains on a CUDA tensor.

## Methods

- **Method 1**: PyTorch Python chain.
- **Method 2**: Libtorch C++ chain.
- **Method 3**: Python emulation with explicit shape/stride checks and launch config.
- **Method 4**: C++ emulation with explicit shape/stride checks and launch config.
- **Method 5A/5B**: C/CUDA bridge for allocator + kernel launch, wired into Python (with/without Numba).

## Python Benchmarks (Method 1/3/5)

```bash
python -m venv .venv
source .venv/bin/activate
pip install torch numba

# Build the bridge (method 5)
python csrc/build_bridge.py
export NUMBA_EVAL_BRIDGE=$(python -c "import csrc.build_bridge as b; print(b.build_bridge())")

# Run python benchmarks
python benchmarks/benchmark.py --device cuda
```

## C++ Benchmarks (Method 2/4)

```bash
# Set TORCH_PATH to your LibTorch install
export Torch_DIR=/path/to/libtorch/share/cmake/Torch
mkdir -p cpp/build
cd cpp/build
cmake ..
cmake --build . -j

./method2_libtorch
./method4_custom
```

## Notes

- The timing is **CPU-only** and does **not** include `cudaDeviceSynchronize`.
- Method 3/4 intentionally keep all checks explicit and unoptimized to emulate compiler-generated code.
- Method 5 uses a CUDA kernel with a C ABI to keep it compatible with Numba's `cfunc` calling convention.
