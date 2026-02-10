import argparse
import json

import method4_api  # type: ignore[import-not-found]
from benchmark import time_cpu  # type: ignore[import-not-found]


LOOPS = 100


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    # Device selection is controlled by which `libcommon` was built/loaded.
    # Keep `--device` for CLI compatibility.
    _ = args.device

    in_ptr = method4_api.create_input()

    out_holder = {"ptr": 0}

    def op() -> None:
        out_holder["ptr"] = int(method4_api.method4(in_ptr))

    seconds = time_cpu(op, 1)
    # Free the final result *after* timing.
    if out_holder["ptr"]:
        method4_api.free_buf(out_holder["ptr"])

    result = {"method4_ms": seconds}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
