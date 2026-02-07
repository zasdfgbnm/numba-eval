import argparse
import json

import method2_nb  # type: ignore[import-not-found]
from benchmark import time_cpu  # type: ignore[import-not-found]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    def op() -> None:
        method2_nb.run_chain(args.device)

    seconds = time_cpu(op, 1)
    result = {"method2_libtorch_nanobind_ms": seconds}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

