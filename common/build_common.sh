#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
OUTPUT="$ROOT_DIR/common/libcommon.so"

nvcc -Xcompiler -fPIC -shared "$ROOT_DIR/common/csrc/add_kernel.cu" -o "$OUTPUT"

echo "$OUTPUT"
