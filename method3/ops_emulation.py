import ctypes
import math
import os
from typing import Sequence, Tuple

import torch

_COMMON_KERNEL = None


def _load_common_kernel() -> ctypes.CDLL:
    global _COMMON_KERNEL
    if _COMMON_KERNEL is not None:
        return _COMMON_KERNEL
    default_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "common", "libcommon.so"))
    so_path = os.environ.get("NUMBA_EVAL_COMMON_SO", default_path)
    if not os.path.exists(so_path):
        raise FileNotFoundError(f"common.so not found at {so_path}")
    lib = ctypes.CDLL(so_path)
    lib.common_launch_add_kernel.argtypes = [
        ctypes.c_uint64,
        ctypes.c_uint64,
        ctypes.c_int64,
        ctypes.c_float,
    ]
    lib.common_launch_add_kernel.restype = None
    _COMMON_KERNEL = lib
    return lib


def _compute_contiguous_stride(shape: Sequence[int]) -> Tuple[int, ...]:
    stride = [1] * len(shape)
    for i in range(len(shape) - 2, -1, -1):
        stride[i] = stride[i + 1] * shape[i + 1]
    return tuple(stride)


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


def _compute_view_stride(shape: Sequence[int], stride: Sequence[int], new_shape: Sequence[int]) -> Tuple[int, ...]:
    if math.prod(shape) != math.prod(new_shape):
        raise ValueError("Reshape numel mismatch.")
    if not shape:
        return ()

    view_stride = [0] * len(new_shape)
    view_dim = len(new_shape) - 1
    chunk_base_stride = stride[-1]
    tensor_numel = 1
    view_numel = 1

    for tensor_dim in range(len(shape) - 1, -1, -1):
        tensor_numel *= shape[tensor_dim]
        at_chunk_end = tensor_dim == 0
        if not at_chunk_end:
            prev_stride = stride[tensor_dim - 1]
            expected = shape[tensor_dim] * stride[tensor_dim]
            if shape[tensor_dim - 1] != 1 and prev_stride != expected:
                at_chunk_end = True

        if at_chunk_end:
            while view_dim >= 0 and (view_numel < tensor_numel or new_shape[view_dim] == 1):
                view_stride[view_dim] = chunk_base_stride * view_numel
                view_numel *= new_shape[view_dim]
                view_dim -= 1
            if view_numel != tensor_numel:
                raise ValueError("Reshape is not viewable without copy.")
            if tensor_dim > 0:
                chunk_base_stride = stride[tensor_dim - 1]
                tensor_numel = 1
                view_numel = 1

    while view_dim >= 0:
        if new_shape[view_dim] != 1:
            raise ValueError("Reshape is not viewable without copy.")
        view_stride[view_dim] = chunk_base_stride * view_numel
        view_numel *= new_shape[view_dim]
        view_dim -= 1

    return tuple(view_stride)


def _calc_launch_config(numel: int, threads_per_block: int = 256) -> Tuple[int, int]:
    blocks = (numel + threads_per_block - 1) // threads_per_block
    return blocks, threads_per_block


def _launch_add(tensor: torch.Tensor, value: float) -> torch.Tensor:
    numel = tensor.numel()
    _calc_launch_config(numel)
    if tensor.device.type != "cuda":
        raise RuntimeError("CUDA tensor required for common kernel")
    output = torch.empty_like(tensor)
    kernel = _load_common_kernel()
    kernel.common_launch_add_kernel(
        ctypes.c_uint64(tensor.data_ptr()),
        ctypes.c_uint64(output.data_ptr()),
        ctypes.c_int64(numel),
        ctypes.c_float(value),
    )
    return output


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
