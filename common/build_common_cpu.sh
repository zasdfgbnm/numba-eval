#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
SRC="$ROOT_DIR/common/csrc/add_cpu.c"

UNAME=$(uname -s)
if [[ "$UNAME" == "Darwin" ]]; then
  OUTPUT="$ROOT_DIR/common/libcommon.dylib"
  cc -O3 -dynamiclib "$SRC" -o "$OUTPUT"
else
  OUTPUT="$ROOT_DIR/common/libcommon.so"
  cc -O3 -fPIC -shared "$SRC" -o "$OUTPUT"
fi

echo "$OUTPUT"

