 # cmake_minimum_required(VERSION 3.30)
project(test_project)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(BoostRoot ${CMAKE_CURRENT_SOURCE_DIR}/boost)
# set(CMAKE_CXX_STANDARD 17)

add_subdirectory(boost)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=gnu++17")

add_executable(main main.cpp)
target_link_libraries(main Boost::asio)