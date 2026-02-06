cmake_minimum_required(VERSION 3.18)
project(method4_custom LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(
  method4_custom
  main.cpp
  common_kernel.cpp
  op_add.cpp
  op_reshape.cpp
)
if(UNIX AND NOT APPLE)
  target_link_libraries(method4_custom dl)
endif()
set_property(TARGET method4_custom PROPERTY CXX_STANDARD 17)
