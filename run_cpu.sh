#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if ! command -v uv >/dev/null 2>&1; then
  echo "error: uv not found. Install it first (see: https://astral.sh/uv/)." >&2
  exit 1
fi

# Work around OpenMP shared-memory issues in some sandboxed environments.
export KMP_DISABLE_SHM=1

# Ensure the in-repo `common/` package is importable even if the project itself
# isn't installed into the environment.
export PYTHONPATH="$ROOT_DIR/common${PYTHONPATH:+:$PYTHONPATH}"

echo "==> Syncing Python environment via uv"
if [[ -f "uv.lock" ]]; then
  uv sync --locked
else
  uv sync
fi

echo
echo "==> Building common CPU kernel library"
PYTHON_BIN="$(uv run python -c 'import sys; print(sys.executable)')"
TORCH_PREFIX="$(uv run python -c 'import torch; print(torch.utils.cmake_prefix_path)')"
cmake -S common -B common/build_cpu \
  -DCMAKE_BUILD_TYPE=Release \
  -DNUMBA_EVAL_USE_CUDA=OFF \
  -DPython3_EXECUTABLE="$PYTHON_BIN" \
  -DCMAKE_PREFIX_PATH="$TORCH_PREFIX" \
  >/dev/null
cmake --build common/build_cpu -j >/dev/null

echo
echo "==> Building nanobind Python extensions (method2/method4)"
rm -rf bindings/build
PYTHON_HEADERS_BIN="$(python3.12 -c 'import sys; print(sys.executable)')"
cmake -S bindings -B bindings/build \
  -DCMAKE_BUILD_TYPE=Release \
  -DPython_EXECUTABLE="$PYTHON_HEADERS_BIN" \
  -DCMAKE_PREFIX_PATH="$TORCH_PREFIX"
cmake --build bindings/build -j

echo
echo "==> Running benchmarks (CPU)"
echo "-- method1 (PyTorch baseline)"
uv run python method1/run.py --device cpu

echo
echo "-- method1.5 (PyTorch + torch.compile)"
uv run python method1.5/run.py --device cpu

echo
echo "-- method2 (LibTorch C++ via nanobind)"
uv run python method2/run.py --device cpu

echo
echo "-- method3 (Python emulation + common kernel)"
uv run python method3/run.py --device cpu

echo
echo "-- method4 (custom emulation C++ via nanobind)"
uv run python method4/run.py --device cpu

echo
echo "-- method5 (method3 + Numba JIT)"
uv run python method5/run.py --device cpu

echo
echo "done."

