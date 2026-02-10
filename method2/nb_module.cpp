#include <nanobind/nanobind.h>

#include <torch/csrc/autograd/python_variable.h>

#include "chain.h"

namespace nb = nanobind;

NB_MODULE(method2_api, m) {
  m.doc() = "nanobind wrapper for method2 (LibTorch C++ baseline)";

  m.def(
      "method2",
      [](nb::handle tensor) {
        method2_libtorch_chain(THPVariable_Unpack(tensor.ptr()));
      },
      nb::arg("tensor"),
      R"doc(
Run the method2 add/reshape chain in C++ (LibTorch).

Notes:
  - loops is fixed in C++.
  - tensor: a PyTorch tensor.
)doc");
}
