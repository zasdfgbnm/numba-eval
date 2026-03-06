cmake_minimum_required(VERSION 3.18)
project(numba_eval_common LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

option(NUMBA_EVAL_USE_CUDA "Build common with CUDA backend" OFF)

# Find Python (for torch cmake prefix discovery if needed).
find_package(Python3 COMPONENTS Interpreter REQUIRED)

# If Torch_DIR / CMAKE_PREFIX_PATH isn't provided, try to discover it from the
# active Python environment (pip/uv/conda torch install).
if(NOT Torch_DIR AND NOT DEFINED CMAKE_PREFIX_PATH)
  execute_process(
    COMMAND "${Python3_EXECUTABLE}" -c "import torch; print(torch.utils.cmake_prefix_path)"
    OUTPUT_VARIABLE _TORCH_PREFIX
    OUTPUT_STRIP_TRAILING_WHITESPACE
    ERROR_QUIET
  )
  if(_TORCH_PREFIX)
    set(CMAKE_PREFIX_PATH "${_TORCH_PREFIX}")
  endif()
endif()

find_package(Torch REQUIRED)

if(NUMBA_EVAL_USE_CUDA)
  enable_language(CUDA)
endif()

add_library(common SHARED)
target_sources(common PRIVATE
  "${CMAKE_CURRENT_LIST_DIR}/csrc/allocate.cpp"
)

if(NUMBA_EVAL_USE_CUDA)
  target_sources(common PRIVATE
    "${CMAKE_CURRENT_LIST_DIR}/csrc/add_kernel.cu"
    "${CMAKE_CURRENT_LIST_DIR}/csrc/normalize_kernel.cu"
  )
  target_compile_definitions(common PRIVATE NUMBA_EVAL_ALLOCATE_DEVICE_CUDA=1)
else()
  target_sources(common PRIVATE
    "${CMAKE_CURRENT_LIST_DIR}/csrc/add_cpu.c"
    "${CMAKE_CURRENT_LIST_DIR}/csrc/normalize_cpu.c"
  )
  target_compile_definitions(common PRIVATE NUMBA_EVAL_ALLOCATE_DEVICE_CPU=1)
endif()

target_include_directories(common PRIVATE ${TORCH_INCLUDE_DIRS})
target_link_libraries(common PRIVATE ${TORCH_LIBRARIES})

# Keep output name/location stable for Python loaders.
set_target_properties(common PROPERTIES
  OUTPUT_NAME "common"
  LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_LIST_DIR}/lib"
  ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_CURRENT_LIST_DIR}/lib"
  RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_LIST_DIR}/lib"
)

