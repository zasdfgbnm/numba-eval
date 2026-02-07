import time
from typing import Callable


def time_cpu(fn: Callable[[], None], iters: int) -> float:
    start = time.perf_counter()
    for _ in range(iters):
        fn()
    end = time.perf_counter()
    return end - start

