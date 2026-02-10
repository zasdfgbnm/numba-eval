cmake_minimum_required(VERSION 3.18)
project(numba_eval_bindings LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Build Python extension modules.
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)

include(FetchContent)

# nanobind (header-only + small support library). Pulled at configure time.
FetchContent_Declare(
  nanobind
  GIT_REPOSITORY https://github.com/wjakob/nanobind.git
  GIT_TAG v2.4.0
)
FetchContent_MakeAvailable(nanobind)

# Torch discovery: if user didn't set Torch_DIR/CMAKE_PREFIX_PATH, try to
# discover it from the active Python environment.
if(NOT Torch_DIR AND NOT DEFINED CMAKE_PREFIX_PATH)
  execute_process(
    COMMAND "${Python_EXECUTABLE}" -c "import torch; print(torch.utils.cmake_prefix_path)"
    OUTPUT_VARIABLE _TORCH_PREFIX
    OUTPUT_STRIP_TRAILING_WHITESPACE
    ERROR_QUIET
  )
  if(_TORCH_PREFIX)
    set(CMAKE_PREFIX_PATH "${_TORCH_PREFIX}")
  endif()
endif()

find_package(Torch REQUIRED)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")

# Put built extension modules under repo_root/common/ so run scripts (PYTHONPATH=common)
# can import them directly.
set(_OUT_DIR "${CMAKE_CURRENT_LIST_DIR}/../common")

# ---- method2 (LibTorch) ----
nanobind_add_module(
  method2_nb
  "${CMAKE_CURRENT_LIST_DIR}/../method2/nb_module.cpp"
  "${CMAKE_CURRENT_LIST_DIR}/../method2/chain.cpp"
)
target_include_directories(method2_nb PRIVATE "${TORCH_INCLUDE_DIRS}")
target_link_libraries(method2_nb PRIVATE "${TORCH_LIBRARIES}"
  "${TORCH_INSTALL_PREFIX}/lib/libtorch_python.so")

if(APPLE OR UNIX)
  # Ensure the Torch shared libraries are discoverable at import time.
  set_target_properties(method2_nb PROPERTIES
    BUILD_RPATH "${TORCH_INSTALL_PREFIX}/lib"
    INSTALL_RPATH "${TORCH_INSTALL_PREFIX}/lib"
  )
endif()

set_target_properties(method2_nb PROPERTIES
  LIBRARY_OUTPUT_DIRECTORY "${_OUT_DIR}"
  RUNTIME_OUTPUT_DIRECTORY "${_OUT_DIR}"
  ARCHIVE_OUTPUT_DIRECTORY "${_OUT_DIR}"
)

# ---- method4 (custom emulation) ----
nanobind_add_module(
  method4_nb
  "${CMAKE_CURRENT_LIST_DIR}/../method4/nb_module.cpp"
  "${CMAKE_CURRENT_LIST_DIR}/../method4/chain.cpp"
  "${CMAKE_CURRENT_LIST_DIR}/../method4/common_kernel.cpp"
  "${CMAKE_CURRENT_LIST_DIR}/../method4/op_add.cpp"
  "${CMAKE_CURRENT_LIST_DIR}/../method4/op_reshape.cpp"
)
target_include_directories(method4_nb PRIVATE "${CMAKE_CURRENT_LIST_DIR}/../method4")

if(UNIX AND NOT APPLE)
  target_link_libraries(method4_nb PRIVATE dl)
endif()

set_target_properties(method4_nb PROPERTIES
  LIBRARY_OUTPUT_DIRECTORY "${_OUT_DIR}"
  RUNTIME_OUTPUT_DIRECTORY "${_OUT_DIR}"
  ARCHIVE_OUTPUT_DIRECTORY "${_OUT_DIR}"
)

