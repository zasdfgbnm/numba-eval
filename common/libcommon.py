"""
Locate the built `libcommon` shared library.

This module provides:
- shared library path discovery (`find_libcommon_path`)
- eager Numba/LLVM initialization + thin wrappers to call the C ABI:
  - `allocate_buf(intp) -> intp`
  - `free_buf(intp) -> void`
  - `add(intp, intp, intp, float32) -> void`

Importing this module will import `numba` / `llvmlite` and load `libcommon`
immediately (fail-fast).
"""

import os
import sys

from llvmlite import binding  # type: ignore[import-not-found]  # noqa: PGH003
from numba import njit  # type: ignore[import-not-found]  # noqa: PGH003
from numba.core import (  # type: ignore[import-not-found]  # noqa: PGH003
    types,
    typing,
)


__all__ = [
    "find_libcommon_path",
    "allocate_buf",
    "free_buf",
    "add",
]


def find_libcommon_path() -> str:
    # Layout: repo_root/common/libcommon.py -> repo_root/common
    common_dir = os.path.abspath(os.path.dirname(__file__))
    if sys.platform == "darwin":
        suffixes = [".dylib", ".so"]
    elif sys.platform.startswith("linux"):
        suffixes = [".so", ".dylib"]
    elif sys.platform == "win32":
        suffixes = [".dll"]
    else:
        raise RuntimeError(f"Unsupported platform: {sys.platform}")

    lib_dir = os.path.join(common_dir, "lib")
    candidates = [
        os.path.join(lib_dir, f"libcommon{suffix}") for suffix in suffixes
    ] + [
        os.path.join(common_dir, f"libcommon{suffix}") for suffix in suffixes
    ]
    lib_path = next((p for p in candidates if os.path.exists(p)), None)
    if lib_path is None:
        raise FileNotFoundError(
            f"common library not found. Tried: {candidates}"
        )
    return lib_path


# ---- Numba / LLVM bindings (eager init) ----

_LIBCOMMON_PATH = find_libcommon_path()

# Load `libcommon` into LLVM at import time (fail-fast).
binding.load_library_permanently(_LIBCOMMON_PATH)

# Use pointer-sized *signed* integers for portability and to match the rest of
# the codebase (`TensorView.ptr` is an `int`).
PTR = types.intp
INT = types.intp
F32 = types.float32

allocate_sig = typing.signature(PTR, INT)
free_sig = typing.signature(types.void, PTR)
add_sig = typing.signature(types.void, PTR, PTR, INT, F32)

# C ABI (ExternalFunction): usable inside nopython functions.
c_allocate_buf = types.ExternalFunction("allocate_buf", allocate_sig)
c_free_buf = types.ExternalFunction("free_buf", free_sig)
c_add = types.ExternalFunction("add", add_sig)


# Thin JIT wrappers (callable from Python too; compile on first call).
@njit(PTR(INT), cache=True, inline="always")
def allocate_buf(num_bytes):
    return c_allocate_buf(num_bytes)


@njit(types.void(PTR), cache=True, inline="always")
def free_buf(ptr):
    c_free_buf(ptr)


@njit(types.void(PTR, PTR, INT, F32), cache=True, inline="always")
def add(inp_ptr, out_ptr, numel, alpha):
    c_add(inp_ptr, out_ptr, numel, alpha)
