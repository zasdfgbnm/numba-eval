#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>

#include "chain.h"

namespace nb = nanobind;

NB_MODULE(method2_nb, m) {
  m.doc() = "nanobind wrapper for method2 (LibTorch C++ baseline)";

  m.def(
      "run_chain",
      [](const std::string& device) { run_method2_libtorch_chain(device); },
      nb::arg("device") = "cpu",
      R"doc(
Run the method2 add/reshape chain in C++ (LibTorch).

Notes:
  - loops is fixed in C++.
  - device: "cpu" or "cuda".
)doc");
}

