from numba import njit  # type: ignore[import-untyped]

from tensor_view import TensorView
from tuple_utils import tuple_set_item


def _get(jit: bool):
    def _prod_ints(xs: tuple[int, ...]) -> int:
        p = 1
        for x in xs:
            p *= int(x)
        return int(p)

    def _infer_size(numel: int, shape: tuple[int, ...]) -> tuple[int, ...]:
        """Return inferred shape tuple, supporting one -1 dim."""
        n = int(len(shape))
        # Keep a fixed-length tuple type for Numba: start from `shape` and
        # only update via `tuple_set_item` when needed.
        inferred = shape
        unknown_dim = -1
        known_product = 1

        for idx in range(n):
            dim = int(shape[idx])
            if dim == -1:
                if unknown_dim != -1:
                    raise ValueError("Only one dimension can be inferred.")
                unknown_dim = idx
            else:
                if dim <= 0:
                    raise ValueError(
                        "Shape dims must be positive or -1 for infer."
                    )
                known_product *= dim

        if unknown_dim != -1:
            if int(numel) % int(known_product) != 0:
                raise ValueError("Inferred dimension is not integral.")
            inferred = tuple_set_item(
                inferred, int(unknown_dim), int(numel) // int(known_product)
            )

        prod = 1
        for i in range(n):
            prod *= int(inferred[i])
        if int(prod) != int(numel):
            raise ValueError("Reshape numel mismatch.")

        return inferred

    def _compute_view_stride(
        shape: tuple[int, ...],
        stride: tuple[int, ...],
        new_shape: tuple[int, ...],
    ) -> tuple[int, ...]:
        """Return view stride as a tuple[int, ...]."""
        if _prod_ints(shape) != _prod_ints(new_shape):
            raise ValueError("Reshape numel mismatch.")

        n = int(len(new_shape))
        view_stride = new_shape
        # Zero-initialize (can't use tuple * int in nopython mode).
        for i in range(n):
            view_stride = tuple_set_item(view_stride, int(i), 0)

        if n == 0:
            return view_stride

        if len(shape) == 0:
            # Scalar view: any reshape with numel==1 is viewable, and the
            # resulting view can be treated as contiguous.
            # Build from the rightmost dim to avoid any in-place updates.
            contig = new_shape
            contig = tuple_set_item(contig, int(n - 1), 1)
            for i in range(n - 2, -1, -1):
                contig = tuple_set_item(
                    contig,
                    int(i),
                    int(contig[i + 1]) * int(new_shape[i + 1]),
                )
            return contig

        view_dim = n - 1
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
                    view_stride = tuple_set_item(
                        view_stride,
                        int(view_dim),
                        int(chunk_base_stride) * int(view_numel),
                    )
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
            view_stride = tuple_set_item(
                view_stride,
                int(view_dim),
                int(chunk_base_stride) * int(view_numel),
            )
            view_numel *= int(new_shape[view_dim])
            view_dim -= 1

        return view_stride

    if jit:
        _prod_ints = njit(_prod_ints, cache=True)
        _infer_size = njit(_infer_size, cache=True)
        _compute_view_stride = njit(_compute_view_stride, cache=True)

    def reshape(view: TensorView, target_shape: tuple[int, ...]) -> TensorView:
        """Return a new TensorView with updated shape/stride."""
        numel = _prod_ints(view.shape)
        out_shape = _infer_size(int(numel), target_shape)
        out_stride = _compute_view_stride(view.shape, view.stride, out_shape)
        return TensorView(ptr=view.ptr, shape=out_shape, stride=out_stride)

    if jit:
        reshape = njit(reshape, cache=True)

    return reshape


reshape = _get(False)
reshape_jit = _get(True)

__all__ = ["reshape", "reshape_jit"]
