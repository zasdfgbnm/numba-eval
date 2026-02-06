import math
from typing import Sequence

from tensor_view import TensorView


def _infer_size(numel: int, shape: Sequence[int]) -> tuple[int, ...]:
    inferred: list[int] = []
    unknown_dim = -1
    known_product = 1
    for idx, dim in enumerate(shape):
        if dim == -1:
            if unknown_dim != -1:
                raise ValueError("Only one dimension can be inferred.")
            unknown_dim = idx
            inferred.append(-1)
        else:
            if dim <= 0:
                raise ValueError(
                    "Shape dims must be positive or -1 for infer."
                )
            known_product *= int(dim)
            inferred.append(int(dim))

    if unknown_dim != -1:
        if numel % known_product != 0:
            raise ValueError("Inferred dimension is not integral.")
        inferred[unknown_dim] = numel // known_product

    if math.prod(inferred) != numel:
        raise ValueError("Reshape numel mismatch.")
    return tuple(int(dim) for dim in inferred)


def _compute_view_stride(
    shape: Sequence[int],
    stride: Sequence[int],
    new_shape: Sequence[int],
) -> tuple[int, ...]:
    if math.prod(shape) != math.prod(new_shape):
        raise ValueError("Reshape numel mismatch.")
    if not shape:
        return ()

    view_stride = [0] * len(new_shape)
    view_dim = len(new_shape) - 1
    chunk_base_stride = int(stride[-1])
    tensor_numel = 1
    view_numel = 1

    for tensor_dim in range(len(shape) - 1, -1, -1):
        tensor_numel *= int(shape[tensor_dim])
        at_chunk_end = tensor_dim == 0
        if not at_chunk_end:
            prev_stride = int(stride[tensor_dim - 1])
            expected = int(shape[tensor_dim]) * int(stride[tensor_dim])
            if int(shape[tensor_dim - 1]) != 1 and prev_stride != expected:
                at_chunk_end = True

        if at_chunk_end:
            while view_dim >= 0 and (
                view_numel < tensor_numel or int(new_shape[view_dim]) == 1
            ):
                view_stride[view_dim] = chunk_base_stride * view_numel
                view_numel *= int(new_shape[view_dim])
                view_dim -= 1
            if view_numel != tensor_numel:
                raise ValueError("Reshape is not viewable without copy.")
            if tensor_dim > 0:
                chunk_base_stride = int(stride[tensor_dim - 1])
                tensor_numel = 1
                view_numel = 1

    while view_dim >= 0:
        if int(new_shape[view_dim]) != 1:
            raise ValueError("Reshape is not viewable without copy.")
        view_stride[view_dim] = chunk_base_stride * view_numel
        view_numel *= int(new_shape[view_dim])
        view_dim -= 1

    return tuple(int(s) for s in view_stride)


def reshape(view: TensorView, target_shape: Sequence[int]) -> TensorView:
    """Return a new TensorView with updated shape/stride (ptr unchanged)."""
    numel = math.prod(view.shape)
    shape = _infer_size(int(numel), target_shape)
    stride = _compute_view_stride(view.shape, view.stride, shape)
    return TensorView(ptr=view.ptr, shape=shape, stride=stride)
