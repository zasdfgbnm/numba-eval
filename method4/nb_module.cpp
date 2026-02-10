#include <nanobind/nanobind.h>

#include "chain.h"

namespace nb = nanobind;

NB_MODULE(method4_api, m) {
  m.doc() = "nanobind wrapper for method4 (custom C++ emulation)";

  m.def(
      "create_input",
      []() -> uint64_t { return method4_create_input(); },
      R"doc(
Allocate the input buffer for the method4 benchmark.

Returns:
  Buffer pointer as an integer.

Notes:
  - Device selection depends on which `libcommon` is available.
)doc");

  m.def(
      "method4",
      [](uint64_t in_ptr) -> uint64_t { return method4_custom_chain(in_ptr); },
      nb::arg("in_ptr"),
      R"doc(
Run the method4 emulation chain in C++.

Returns:
  Output buffer pointer as an integer (caller must free).

Notes:
  - loops is fixed in C++.
  - Device selection depends on which `libcommon` is available.
)doc");

  m.def(
      "free_buf",
      [](uint64_t ptr) { method4_free_buf(ptr); },
      nb::arg("ptr"),
      R"doc(
Free a buffer allocated by create_input or returned by method4.
)doc");
}
