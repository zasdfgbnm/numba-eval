import argparse
import json
import math
from typing import Sequence

from benchmark import time_cpu  # type: ignore[import-not-found]
from allocate import allocate, free  # type: ignore[import-not-found]
from chain import (  # type: ignore[import-not-found]
    SHAPE_B,
    emulate_add_reshape_chain,
)
from tensor_view import TensorView  # type: ignore[import-not-found]


LOOPS = 100


def _contiguous_stride(shape: Sequence[int]) -> tuple[int, ...]:
    stride = [1] * len(shape)
    for i in range(len(shape) - 2, -1, -1):
        stride[i] = stride[i + 1] * int(shape[i + 1])
    return tuple(int(s) for s in stride)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    # Device selection is controlled by which `libcommon` was built/loaded.
    # Keep `--device` for CLI compatibility.
    _ = args.device

    numel = int(math.prod(SHAPE_B))
    in_ptr = allocate(numel * 4)  # float32 bytes
    in_shape = tuple(int(d) for d in SHAPE_B)
    in_stride = _contiguous_stride(SHAPE_B)

    # Inline the timed op into main().
    view = TensorView(ptr=in_ptr, shape=in_shape, stride=in_stride)

    def op() -> None:
        nonlocal view
        for _ in range(LOOPS):
            old_ptr = view.ptr
            view = emulate_add_reshape_chain(view)
            free(old_ptr)

    seconds = time_cpu(op, 1)
    # Free the final result *after* timing.
    free(view.ptr)

    result = {"method3_python_emulation": seconds}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
