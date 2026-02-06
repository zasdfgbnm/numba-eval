from allocate import free
from add import add
from reshape import reshape
from tensor_view import TensorView

# Keep these constants in one place so method3 and method4 stay aligned.
SHAPE_A = (19, 17, 13, 11, 7, 5, 3, 2)
SHAPE_B = (2, 3, 5, 7, 11, 13, 17, 19)


def emulate_add_reshape_chain(inp: TensorView) -> TensorView:
    """Emulate add/reshape chain on a TensorView."""
    tmp1 = add(inp, 1.0)
    v1 = reshape(tmp1, SHAPE_A)
    tmp2 = add(v1, -1.0)
    free(tmp1.ptr)

    v2 = reshape(tmp2, SHAPE_B)
    tmp3 = add(v2, 0.0)
    free(tmp2.ptr)
    return tmp3
