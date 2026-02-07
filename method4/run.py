import argparse
import json

import method4_nb  # type: ignore[import-not-found]
from benchmark import time_cpu  # type: ignore[import-not-found]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    # Device selection is controlled by which `libcommon` was built/loaded.
    # Keep `--device` for CLI compatibility.
    _ = args.device

    def op() -> None:
        method4_nb.run_chain()

    seconds = time_cpu(op, 1)
    result = {"method4_custom_nanobind_seconds": seconds}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

