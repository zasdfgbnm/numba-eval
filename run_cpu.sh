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
bash ./common/build_common_cpu.sh >/dev/null

echo
echo "==> Running Python scripts (CPU)"
echo "-- method1 (PyTorch baseline)"
uv run python method1/run.py --device cpu

echo
echo "-- method3 (Python emulation)"
uv run python method3/run.py --device cpu

echo
echo "-- method5 (ctypes CPU fallback)"
uv run python method5/run.py --device cpu

echo
echo "==> Building & running C++ benchmarks (CPU) if Torch_DIR is set"
if [[ -n "${Torch_DIR:-}" ]]; then
  echo "-- method2 (LibTorch C++)"
  rm -rf method2/build
  cmake -S method2 -B method2/build -DCMAKE_BUILD_TYPE=Release
  cmake --build method2/build -j
  ./method2/build/method2_libtorch --device cpu

  echo
  echo "-- method4 (custom emulation C++)"
  rm -rf method4/build
  cmake -S method4 -B method4/build -DCMAKE_BUILD_TYPE=Release
  cmake --build method4/build -j
  ./method4/build/method4_custom --device cpu
else
  echo "Skipping method2/method4: set Torch_DIR to your libtorch cmake dir to enable."
fi

echo
echo "done."

