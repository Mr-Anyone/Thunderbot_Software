message(Configuring Protobuf)

#see: https://github.com/nanopb/nanopb/blob/master/extra/FindNanopb.cmake#L54
list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/vendor/nanopb/extra)
set(PROTOBUF_PROTOC_EXECUTABLE "C:\\Program Files (x86)\\Thunderbots\\bin\\protoc")
set(PROTOC_OPTIONS --include_imports --descriptor_set_out)
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
NANOPB_GENERATE_CPP(TBOTS_PROTO_PROTO_SRCS TBOTS_PROTO_PROTO_HDRS RELPATH .  ${TBOTS_PROTO_SRCS})

add_library(tbots_proto SHARED STATIC ${GOOGLE_PB_SRC} ${GOOGLE_PB_HD} ${TBOTS_PROTO_PROTO_SRCS} ${TBOTS_PROTO_PROTO_HDRS})
target_include_directories(tbots_proto INTERFACE  
    ${CMAKE_CURRENT_BINARY_DIR}
    ${NANOPB_INCLUDE_DIRS}
)

# building tbots ssl proto
SET(TBOTS_SSL_PROTO_SRC 
    ssl_autoref_ci.proto
    ssl_gc_api.proto
    ssl_gc_change.proto
    ssl_gc_ci.proto
    ssl_gc_common.proto
    ssl_gc_engine.proto
    ssl_gc_engine_config.proto
    ssl_gc_game_event.proto
    ssl_gc_geometry.proto
    ssl_gc_referee_message.proto
    ssl_gc_state.proto
    ssl_vision_detection.proto
    ssl_vision_detection_tracked.proto
    ssl_vision_geometry.proto
    ssl_vision_wrapper.proto
    ssl_vision_wrapper_tracked.proto
)
NANOPB_GENERATE_CPP(TBOTS_SSL_PROTO_SRCS TBOTS_SSL_PROTO_PROTO_HDRS  ${TBOTS_SSL_PROTO_SRC})

add_library(tbots_ssl_proto SHARED STATIC ${TBOTS_SSL_PROTO_SRCS} ${TBOTS_SSL_PROTO_PROTO_HDRS})
target_include_directories(tbots_ssl_proto INTERFACE  
   ${CMAKE_CURRENT_BINARY_DIR}
   ${NANOPB_INCLUDE_DIRS}
)

# compiling/testing tbots_protobuf
message(Done Configuring Protobuf)