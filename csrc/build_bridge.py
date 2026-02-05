import os
from torch.utils.cpp_extension import CUDAExtension, load


def build_bridge() -> str:
    sources = [os.path.join(os.path.dirname(__file__), "bridge.cpp"), os.path.join(os.path.dirname(__file__), "add_kernel.cu")]
    module = load(
        name="numba_eval_bridge",
        sources=sources,
        verbose=True,
        extra_cuda_cflags=["--use_fast_math"],
    )
    return module.__file__


if __name__ == "__main__":
    path = build_bridge()
    print(path)
