cmake_minimum_required(VERSION 3.26.6)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_C_STANDARD 17)

project(Thunderbots VERSION 1.0)

add_subdirectory(vendor)
add_subdirectory(src)

add_executable(test_proto_build test_build.cpp)
target_link_libraries(test_proto_build PRIVATE tbots_proto)