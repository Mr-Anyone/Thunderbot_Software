package(default_visibility = ["//visibility:public"])

load("@thunderscope_deps//:requirements.bzl", "requirement")

py_binary(
    name = "recover_zip",
    srcs = ["recover_zip.py"],
    deps = [
        "proto_logger",
        "proto_player",
        "//software/thunderscope:proto_unix_io",
        "//proto:software_py_proto",
        "//proto/message_translation:py_tbots_protobuf",
        "//extlibs/er_force_sim/src/protobuf:erforce_py_proto",
    ]
)

py_library(
    name = "proto_logger",
    srcs = [
        "proto_logger.py",
        "replay_constants.py",
    ],
    deps = [
        requirement("pyqtgraph"),
    ],
)

py_library(
    name = "proto_player",
    srcs = [
        "proto_player.py",
        "replay_constants.py",
    ],
    deps = [
        requirement("pyqtgraph"),
    ],
)

py_library(
    name = "replay_controls",
    srcs = [
        "replay_controls.py",
    ],
    deps = [
        requirement("pyqtgraph"),
        ":proto_player",
    ],
)
