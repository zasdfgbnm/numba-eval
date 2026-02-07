#include <nanobind/nanobind.h>

#include "chain.h"

namespace nb = nanobind;

NB_MODULE(method4_nb, m) {
  m.doc() = "nanobind wrapper for method4 (custom C++ emulation)";

  m.def(
      "run_chain",
      []() { run_method4_custom_chain(); },
      R"doc(
Run the method4 emulation chain in C++.

Notes:
  - loops is fixed in C++.
  - Device selection depends on which `libcommon` is available.
)doc");
}

