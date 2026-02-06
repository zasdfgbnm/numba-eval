import ctypes
import os
import sys


def _load_libcommon_path() -> str:
    # Layout: repo_root/common/_C.py -> repo_root/common
    common_dir = os.path.abspath(os.path.dirname(__file__))
    if sys.platform == "darwin":
        suffixes = [".dylib"]
    elif sys.platform.startswith("linux"):
        suffixes = [".so"]
    elif sys.platform == "win32":
        suffixes = [".dll"]
    else:
        raise RuntimeError(f"Unsupported platform: {sys.platform}")

    candidates = [
        os.path.join(common_dir, f"libcommon{suffix}") for suffix in suffixes
    ]
    lib_path = next((p for p in candidates if os.path.exists(p)), None)
    if lib_path is None:
        raise FileNotFoundError(
            f"common library not found. Tried: {candidates}"
        )
    return lib_path


_LIBCOMMON_PATH = _load_libcommon_path()
_C = ctypes.CDLL(_LIBCOMMON_PATH)

# C ABI:
#   uint64_t allocate_buf(int64_t num_bytes)
#   void free_buf(uint64_t ptr)
#   void add(const float* input, float* output, int64_t numel, float alpha)
_C.allocate_buf.argtypes = [ctypes.c_int64]
_C.allocate_buf.restype = ctypes.c_uint64
_C.free_buf.argtypes = [ctypes.c_uint64]
_C.free_buf.restype = None
_C.add.argtypes = [
    ctypes.c_uint64,  # input ptr
    ctypes.c_uint64,  # output ptr
    ctypes.c_int64,  # numel
    ctypes.c_float,  # alpha
]
_C.add.restype = None
