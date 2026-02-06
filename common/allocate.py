from libcommon import allocate_buf, free_buf  # type: ignore[import-not-found]


def allocate(num_bytes: int) -> int:
    """Allocate `num_bytes` and return a raw data pointer (uint64)."""
    if num_bytes < 0:
        raise ValueError(f"num_bytes must be >= 0, got {num_bytes}")

    return int(allocate_buf(num_bytes))


def free(ptr: int) -> None:
    """Release a pointer previously returned by `allocate`."""
    free_buf(ptr)
