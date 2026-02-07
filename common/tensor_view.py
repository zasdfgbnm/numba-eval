from typing import NamedTuple

from typing import Tuple


class TensorView(NamedTuple):
    ptr: int
    shape: Tuple[int, ...]
    stride: Tuple[int, ...]
