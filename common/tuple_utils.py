"""
Tuple helpers that work in both Python and Numba nopython mode.

The primary goal is to replace in-place ndarray updates like:
  stride[i] = x
with a persistent tuple update:
  stride = tuple_set_item(stride, i, x)
"""

from __future__ import annotations

from typing import Any, Tuple, TypeVar

T = TypeVar("T")


def tuple_set_item(t: Tuple[T, ...], i: int, x: T) -> Tuple[T, ...]:
    """Return a new tuple with element at index `i` replaced by `x`.

    - Supports negative indices (Python semantics).
    - Raises IndexError if out of range.
    """
    n = len(t)
    if i < 0:
        i += n
    if i < 0 or i >= n:
        raise IndexError("tuple index out of range")
    # Pure-Python fallback (also fine outside JIT).
    return t[:i] + (x,) + t[i + 1:]


# ---- Numba specialization (optional) ----
#
# For nopython mode we cannot rely on dynamic tuple slicing with runtime `i`
# because the output tuple type/length must be known at compile time.
# Instead, we generate an explicit if/elif ladder over all positions for the
# tuple length inferred from the input tuple type.
try:  # pragma: no cover (covered indirectly when numba is installed)
    from numba import types  # type: ignore[import-untyped]
    from numba.extending import overload  # type: ignore[import-untyped]
except Exception:  # pragma: no cover
    overload = None  # type: ignore[assignment]
    types = None  # type: ignore[assignment]


def _make_tuple_set_item_impl(n: int):
    # Generate a small, branchy function so Numba can compile it to native code
    # without any heap allocation / NRT involvement for pure numeric tuples.
    lines = [
        "def impl(t, i, x):",
        f"    n = {int(n)}",
        "    if i < 0:",
        "        i += n",
        "    if i < 0 or i >= n:",
        '        raise IndexError("tuple index out of range")',
    ]

    for k in range(n):
        # Build: (t[0], ..., x, ..., t[n-1])
        elems = ", ".join("x" if j == k else f"t[{j}]" for j in range(n))
        if n == 1:
            elems += ","
        head = "    if" if k == 0 else "    elif"
        lines.append(f"{head} i == {k}:")
        lines.append(f"        return ({elems})")

    # Should be unreachable due to bounds check above.
    lines.append('    raise IndexError("tuple index out of range")')

    ns: dict[str, Any] = {}
    exec("\n".join(lines), ns, ns)
    return ns["impl"]


if overload is not None:

    @overload(tuple_set_item)  # type: ignore[misc]
    def _ov_tuple_set_item(t, i, x):
        if not isinstance(t, types.BaseTuple):  # type: ignore[union-attr]
            return None
        n = len(t)
        impl = _make_tuple_set_item_impl(n)
        return impl


__all__ = ["tuple_set_item"]
