cmake_minimum_required(VERSION 3.30)
project(test_project)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(BoostRoot ${CMAKE_CURRENT_SOURCE_DIR}/boost)
add_subdirectory(boost)

add_executable(main main.cpp)
target_link_libraries(main Boost::asio)