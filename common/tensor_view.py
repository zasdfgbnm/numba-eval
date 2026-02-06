from typing import NamedTuple


class TensorView(NamedTuple):
    ptr: int
    shape: tuple[int, ...]
    stride: tuple[int, ...]

