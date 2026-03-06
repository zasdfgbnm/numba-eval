import argparse
import json
import math

from numba import njit  # type: ignore[import-untyped]

from benchmark import time_cpu  # type: ignore[import-not-found]
from allocate import allocate_jit as allocate  # type: ignore[import-not-found]
from allocate import free_jit as free  # type: ignore[import-not-found]
from chain import (  # type: ignore[import-not-found]
    emulate_normalize_reshape_chain_jit as emulate_normalize_reshape_chain,
)
from stride import contiguous_stride  # type: ignore[import-not-found]
from tensor_view import TensorView  # type: ignore[import-not-found]


@njit(cache=True, inline="always")
def method5(view: TensorView) -> TensorView:
    for i in range(100):
        old_ptr = view.ptr
        view = emulate_normalize_reshape_chain(view, i)
        free(old_ptr)
    return view


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    # Device selection is controlled by which `libcommon` was built/loaded.
    # Keep `--device` for CLI compatibility.
    _ = args.device

    numel = int(math.prod((2, 3, 5, 7, 11, 13, 17, 19)))
    in_ptr = allocate(numel * 4)  # float32 bytes
    in_view = TensorView(ptr=in_ptr, shape=(2, 3, 5, 7, 11, 13, 17, 19), stride=contiguous_stride((2, 3, 5, 7, 11, 13, 17, 19)))

    # Warm up JIT compilation outside timing.
    warm_ptr = allocate(numel * 4)
    warm_view = TensorView(ptr=warm_ptr, shape=(2, 3, 5, 7, 11, 13, 17, 19), stride=contiguous_stride((2, 3, 5, 7, 11, 13, 17, 19)))
    warm_out = method5(warm_view)
    free(warm_out.ptr)

    out_holder = {"view": in_view}

    def op() -> None:
        out_holder["view"] = method5(in_view)

    seconds = time_cpu(op, 1)
    # Free the final result *after* timing.
    if out_holder["view"].ptr:
        free(out_holder["view"].ptr)

    result = {"method5_ms": seconds}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
