cmake_minimum_required(VERSION 3.18)
project(method2_libtorch LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Torch REQUIRED)

add_executable(method2_libtorch main.cpp)
target_link_libraries(method2_libtorch "${TORCH_LIBRARIES}")
set_property(TARGET method2_libtorch PROPERTY CXX_STANDARD 17)

if (MSVC)
  file(GLOB TORCH_DLLS "${TORCH_INSTALL_PREFIX}/lib/*.dll")
  add_custom_command(TARGET method2_libtorch
      POST_BUILD
      COMMAND ${CMAKE_COMMAND} -E copy_if_different
      ${TORCH_DLLS}
      $<TARGET_FILE_DIR:method2_libtorch>)
endif (MSVC)
