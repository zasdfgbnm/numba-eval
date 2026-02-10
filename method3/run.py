import argparse
import json
import math

from benchmark import time_cpu  # type: ignore[import-not-found]
from allocate import allocate, free  # type: ignore[import-not-found]
from chain import (  # type: ignore[import-not-found]
    SHAPE_B,
    emulate_add_reshape_chain,
)
from stride import contiguous_stride  # type: ignore[import-not-found]
from tensor_view import TensorView  # type: ignore[import-not-found]


LOOPS = 100


def method3(view: TensorView) -> TensorView:
    for _ in range(LOOPS):
        old_ptr = view.ptr
        view = emulate_add_reshape_chain(view)
        free(old_ptr)
    return view


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    # Device selection is controlled by which `libcommon` was built/loaded.
    # Keep `--device` for CLI compatibility.
    _ = args.device

    numel = int(math.prod(SHAPE_B))
    in_ptr = allocate(numel * 4)  # float32 bytes
    in_view = TensorView(ptr=in_ptr, shape=SHAPE_B, stride=contiguous_stride(SHAPE_B))

    out_holder = {"view": in_view}

    def op() -> None:
        out_holder["view"] = method3(in_view)

    seconds = time_cpu(op, 1)
    # Free the final result *after* timing.
    free(out_holder["view"].ptr)

    result = {"method3_ms": seconds}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
