package(default_visibility = ["//visibility:public"])


py_library(
    name = "proto_logger",
    srcs = [
        "proto_logger.py",
        "replay_constants.py",
    ],
    deps = [
    ],
)

py_library(
    name = "proto_player",
    srcs = [
        "proto_player.py",
        "replay_constants.py",
    ],
    deps = [
    ],
)

py_library(
    name = "replay_controls",
    srcs = [
        "replay_controls.py",
    ],
    deps = [
        ":proto_player",
    ],
)
