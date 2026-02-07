import time
from typing import Callable


def time_cpu(
    fn: Callable[[], None],
    iters: int,
    warmup: int = 5,
    reps: int = 10,
) -> float:
    for _ in range(warmup):
        fn()

    total = 0.0
    for _ in range(reps):
        start = time.perf_counter()
        for _ in range(iters):
            fn()
        end = time.perf_counter()
        total += end - start
    return (total / reps) * 1000.0

