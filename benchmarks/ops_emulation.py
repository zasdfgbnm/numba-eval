import math
from dataclasses import dataclass
from typing import List, Sequence, Tuple

import torch


@dataclass
class ShapeStride:
    shape: Tuple[int, ...]
    stride: Tuple[int, ...]

    @property
    def numel(self) -> int:
        numel = 1
        for dim in self.shape:
            numel *= dim
        return numel


def _compute_contiguous_stride(shape: Sequence[int]) -> Tuple[int, ...]:
    stride = [1] * len(shape)
    for i in range(len(shape) - 2, -1, -1):
        stride[i] = stride[i + 1] * shape[i + 1]
    return tuple(stride)


def _is_contiguous(shape: Sequence[int], stride: Sequence[int]) -> bool:
    return tuple(stride) == _compute_contiguous_stride(shape)


def _infer_size(numel: int, shape: Sequence[int]) -> Tuple[int, ...]:
    inferred = []
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
                raise ValueError("Shape dims must be positive or -1 for infer.")
            known_product *= dim
            inferred.append(dim)
    if unknown_dim != -1:
        if numel % known_product != 0:
            raise ValueError("Inferred dimension is not integral.")
        inferred[unknown_dim] = numel // known_product
    if math.prod(inferred) != numel:
        raise ValueError("Reshape numel mismatch.")
    return tuple(int(dim) for dim in inferred)


def _can_view(shape: Sequence[int], stride: Sequence[int], new_shape: Sequence[int]) -> bool:
    """Emulate PyTorch view/reshape compatibility checks."""
    if math.prod(shape) != math.prod(new_shape):
        return False
    if _is_contiguous(shape, stride):
        return True

    # Collapse contiguous chunks and verify they can be reinterpreted.
    dims = list(shape)
    strides = list(stride)
    view_dims = []
    view_strides = []
    for size, st in zip(dims, strides):
        if size == 1:
            continue
        if view_dims and view_strides[-1] == st * size:
            view_dims[-1] *= size
        else:
            view_dims.append(size)
            view_strides.append(st)

    # If the collapsed representation is contiguous, accept.
    if not view_dims:
        return True

    expected = _compute_contiguous_stride(view_dims)
    return tuple(view_strides) == expected


def _compute_view_stride(shape: Sequence[int], stride: Sequence[int], new_shape: Sequence[int]) -> Tuple[int, ...]:
    if not _can_view(shape, stride, new_shape):
        raise ValueError("Reshape is not viewable without copy.")
    return _compute_contiguous_stride(new_shape)


def _calc_launch_config(numel: int, threads_per_block: int = 256) -> Tuple[int, int]:
    blocks = (numel + threads_per_block - 1) // threads_per_block
    return blocks, threads_per_block


def _launch_add(tensor: torch.Tensor, value: float) -> torch.Tensor:
    numel = tensor.numel()
    contiguous = tensor.is_contiguous()
    _ = contiguous  # emulate compiler-generated checks
    _calc_launch_config(numel)
    return tensor.add(value)


def reshape_with_checks(tensor: torch.Tensor, target_shape: Sequence[int]) -> torch.Tensor:
    shape = tuple(int(dim) for dim in tensor.shape)
    stride = tuple(int(dim) for dim in tensor.stride())
    numel = math.prod(shape)
    inferred = _infer_size(numel, target_shape)
    target_stride = _compute_view_stride(shape, stride, inferred)
    return torch.as_strided(tensor, size=inferred, stride=target_stride)


def emulate_add_reshape_chain(tensor: torch.Tensor, shape_a: Sequence[int], shape_b: Sequence[int]) -> torch.Tensor:
    out = _launch_add(tensor, 1.0)
    out = reshape_with_checks(out, shape_a)
    out = _launch_add(out, -1.0)
    out = reshape_with_checks(out, shape_b)
    out = _launch_add(out, 0.0)
    return out
