from numba import njit  # type: ignore[import-untyped]

from allocate import free, free_jit
from normalize import normalize, normalize_jit
from reshape import reshape, reshape_jit
from tensor_view import TensorView


def _get(jit: bool):
    _normalize = normalize_jit if jit else normalize
    _reshape = reshape_jit if jit else reshape
    _free = free_jit if jit else free

    def emulate_normalize_reshape_chain(inp: TensorView, i: int) -> TensorView:
        """Emulate normalize/reshape chain on a TensorView."""
        v1 = _reshape(inp, (19, 17, 13, 11, 7, 5, 3, 2))
        tmp1 = _normalize(v1, int(i) % 4)

        v2 = _reshape(tmp1, (2, 3, 5, 7, 11, 13, 17, 19))
        return v2

    if jit:
        emulate_normalize_reshape_chain = njit(
            emulate_normalize_reshape_chain, cache=True, inline="always"
        )

    return emulate_normalize_reshape_chain


emulate_normalize_reshape_chain = _get(False)
emulate_normalize_reshape_chain_jit = _get(True)

__all__ = [
    "emulate_normalize_reshape_chain",
    "emulate_normalize_reshape_chain_jit",
]
