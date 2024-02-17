message("Configuring Protobuf")

#see: https://github.com/nanopb/nanopb/blob/master/extra/FindNanopb.cmake#L54
list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/vendor/nanopb/extra)
find_package(Nanopb REQUIRED)
include_directories(${NANOPB_INCLUDE_DIRS})
include_directories(${CMAKE_CURRENT_BINARY_DIR})
# see: https://dominikberner.ch/cmake-interface-lib/
include(GNUInstallDirs)


# build and generating protobufs
# these are our sources files
# create tbots proto sources
set(TBOTS_PROTO_SRCS 
    ball.proto
    game_state.proto
    geneva_slot.proto
    geometry.proto
    parameters.proto
    play.proto
    power_frame_msg.proto
    primitive.proto
    robot_crash_msg.proto
    robot_log_msg.proto
    robot_status_msg.proto
    tactic.proto
    tbots_software_msgs.proto
    tbots_timestamp_msg.proto
    team.proto
    vision.proto
    world.proto
)
NANOPB_GENERATE_CPP(PROTO_SRCS PROTO_HDRS RELPATH . ${TBOTS_PROTO_SRCS})

add_library(tbots_proto SHARED STATIC ${PROTO_SRCS} ${PROTO_HDRS})
target_include_directories(tbots_proto INTERFACE  
    ${CMAKE_CURRENT_BINARY_DIR}
    ${NANOPB_INCLUDE_DIRS}
)

# compiling/testing tbots_protobuf
message("Done Configuring Protobuf")