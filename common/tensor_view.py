from typing import NamedTuple

import numpy as np


class TensorView(NamedTuple):
    ptr: int
    shape: np.ndarray
    stride: np.ndarray
