import argparse
import json
import math
from typing import Tuple

from numba import njit  # type: ignore[import-not-found]

from benchmark import time_cpu  # type: ignore[import-not-found]
from allocate import allocate, free  # type: ignore[import-not-found]
from chain import (  # type: ignore[import-not-found]
    SHAPE_B,
    emulate_add_reshape_chain,
)
from tensor_view import TensorView  # type: ignore[import-not-found]


LOOPS = 100


def _contiguous_stride(shape: Tuple[int, ...]) -> Tuple[int, ...]:
    stride = [1] * len(shape)
    for i in range(len(shape) - 2, -1, -1):
        stride[i] = stride[i + 1] * int(shape[i + 1])
    return tuple(int(s) for s in stride)


_STRIDE_B = _contiguous_stride(SHAPE_B)


@njit(cache=True)
def run_loops(ptr: int) -> int:
    view = TensorView(ptr=ptr, shape=SHAPE_B, stride=_STRIDE_B)
    for _ in range(LOOPS):
        old_ptr = view.ptr
        view = emulate_add_reshape_chain(view)
        free(old_ptr)
    return view.ptr


def method5_numba(in_ptr: int, numel: int) -> Tuple[float, int, str]:
    # Warm up compilation outside timing.
    warm_ptr = allocate(numel * 4)
    warm_out = int(run_loops(warm_ptr))
    free(warm_out)

    out_holder = {"ptr": 0}

    def op() -> None:
        out_holder["ptr"] = int(run_loops(in_ptr))

    seconds = time_cpu(op, 1)
    return seconds, int(out_holder["ptr"]), "ok"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    # Device selection is controlled by which `libcommon` was built/loaded.
    # Keep `--device` for CLI compatibility.
    _ = args.device

    numel = int(math.prod(SHAPE_B))
    in_ptr = allocate(numel * 4)  # float32 bytes
    seconds, out_ptr, note = method5_numba(in_ptr, numel)
    if out_ptr:
        free(out_ptr)
    result = {"method5_numba_jit": seconds, "method5_note": note}

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
