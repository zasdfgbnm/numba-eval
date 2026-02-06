import os
from torch.utils.cpp_extension import load


def build_bridge() -> str:
    base_dir = os.path.dirname(__file__)
    sources = [os.path.join(base_dir, "csrc", "bridge.cpp")]
    module = load(
        name="numba_eval_bridge",
        sources=sources,
        verbose=True,
    )
    return module.__file__


if __name__ == "__main__":
    path = build_bridge()
    print(path)
