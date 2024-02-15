message("Configuring Protobuf")

#see: https://github.com/nanopb/nanopb/blob/master/extra/FindNanopb.cmake#L54
list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/vendor/nanopb/extra)

find_package(Nanopb REQUIRED)
include_directories(${NANOPB_INCLUDE_DIRS})

# build and generating protobufs
file(GLOB proto_srcs *.proto)
set(protobuf_MSVC_STATIC_RUNTIME OFF)
NANOPB_GENERATE_CPP(PROTO_SRCS PROTO_HDRS  ${proto_srcs})

include_directories(${CMAKE_CURRENT_BINARY_DIR})

# compiling tbots_protobuf
add_library(tbots_proto STATIC ${PROTO_SRCS} ${PROTO_HDRS})
target_link_libraries(tbots_proto PUBLIC libprotobuf)

# adding a test script to make sure things are successfully complied
add_executable(test_proto_build test_build.cpp)
target_link_libraries(test_proto_build libprotobuf)
message("Done Configuring Protobuf")
