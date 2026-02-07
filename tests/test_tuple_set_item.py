import os
import re
import sys

import pytest
from numba import njit  # type: ignore[import-untyped]


# This repo uses a "flat" module layout with `package-dir = {"" = "common"}`.
# For tests executed from the repo root without installation, add `common/`.
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
COMMON_DIR = os.path.join(REPO_ROOT, "common")
if COMMON_DIR not in sys.path:
    sys.path.insert(0, COMMON_DIR)


from tuple_utils import tuple_set_item  # type: ignore[import-not-found]  # noqa: E402


def test_tuple_set_item_python_semantics():
    t = (1, 2, 3)
    assert tuple_set_item(t, 0, 9) == (9, 2, 3)
    assert tuple_set_item(t, 1, 9) == (1, 9, 3)
    assert tuple_set_item(t, 2, 9) == (1, 2, 9)
    assert tuple_set_item(t, -1, 9) == (1, 2, 9)


def test_tuple_set_item_python_raises():
    with pytest.raises(IndexError):
        tuple_set_item((), 0, 1)
    with pytest.raises(IndexError):
        tuple_set_item((1, 2, 3), 3, 0)
    with pytest.raises(IndexError):
        tuple_set_item((1, 2, 3), -4, 0)


def test_tuple_set_item_numba_correctness():
    @njit(cache=True)
    def f():
        t = (1, 2, 3, 4)
        for i in range(4):
            t = tuple_set_item(t, i, i + 10)
        return t

    @njit(cache=True)
    def g():
        t = (1, 2, 3)
        return tuple_set_item(t, -1, 99)

    assert f() == (10, 11, 12, 13)
    assert g() == (1, 2, 99)


def test_tuple_set_item_numba_no_nrt_allocations():
    # Heuristic check: for pure numeric tuples, the compiled IR should not
    # involve Numba's NRT heap allocations.
    @njit(cache=True)
    def f(i: int):
        t = (1, 2, 3, 4)
        return tuple_set_item(t, i, 7)

    # Numba disables inspection when loading *from* disk cache. To keep
    # `cache=True` (fast for normal use) while still inspecting LLVM reliably
    # in this test, flush any existing cache entries for this function.
    cache = getattr(f, "_cache", None)
    if cache is not None and hasattr(cache, "flush"):
        cache.flush()

    # Compile for a concrete signature.
    assert f(2) == (1, 2, 7, 4)
    sig = f.signatures[0]
    llvm = f.inspect_llvm(sig)

    # `inspect_llvm()` returns a whole LLVM module including CPython wrappers
    # that legitimately call Python C-API and NRT. We only care about the
    # native nopython function body.
    native_name = f.overloads[sig].fndesc.llvm_func_name
    m = re.search(
        r"define[^\n]*@"
        + re.escape(native_name)
        + r"\b[\s\S]*?\n}\n",
        llvm,
    )
    assert m is not None, f"failed to locate native function body for {native_name}"
    native_llvm = m.group(0)

    banned_call_patterns = [
        r"\bcall\b.*@NRT_",
        r"\bcall\b.*@malloc\b",
        r"\bcall\b.*@free\b",
    ]

    call_lines = [
        ln
        for ln in native_llvm.splitlines()
        if " call " in ln or ln.lstrip().startswith("call ")
    ]
    hits = []
    for pat in banned_call_patterns:
        rx = re.compile(pat)
        hits.extend([ln for ln in call_lines if rx.search(ln)])

    assert hits == [], (
        "unexpected heap/NRT call(s) in native LLVM:\n" + "\n".join(hits)
    )

