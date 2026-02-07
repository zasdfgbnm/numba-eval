from numba import njit  # type: ignore[import-untyped]

from allocate import free, free_jit
from add import add, add_jit
from reshape import reshape, reshape_jit
from tensor_view import TensorView

# Keep these constants in one place so method3 and method4 stay aligned.
SHAPE_A = (19, 17, 13, 11, 7, 5, 3, 2)
SHAPE_B = (2, 3, 5, 7, 11, 13, 17, 19)


def _get(jit: bool):
    _add = add_jit if jit else add
    _reshape = reshape_jit if jit else reshape
    _free = free_jit if jit else free

    def emulate_add_reshape_chain(inp: TensorView) -> TensorView:
        """Emulate add/reshape chain on a TensorView."""
        tmp1 = _add(inp, 1.0)
        v1 = _reshape(tmp1, SHAPE_A)
        tmp2 = _add(v1, -1.0)
        _free(tmp1.ptr)

        v2 = _reshape(tmp2, SHAPE_B)
        tmp3 = _add(v2, 0.0)
        _free(tmp2.ptr)
        return tmp3

    if jit:
        emulate_add_reshape_chain = njit(emulate_add_reshape_chain, cache=True)

    return emulate_add_reshape_chain


emulate_add_reshape_chain = _get(False)
emulate_add_reshape_chain_jit = _get(True)

__all__ = [
    "SHAPE_A",
    "SHAPE_B",
    "emulate_add_reshape_chain",
    "emulate_add_reshape_chain_jit",
]
