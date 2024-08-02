package(default_visibility = ["//visibility:public"])


py_library(
    name = "gl_toolbar",
    srcs = ["gl_toolbar.py"],
    deps = [
    ],
)

py_library(
    name = "icon_loader",
    srcs = ["icon_loader.py"],
    deps = [
    ],
)

py_library(
    name = "gl_field_toolbar",
    srcs = ["gl_field_toolbar.py"],
    deps = [
        ":gl_toolbar",
        "//software/thunderscope/common:common_widgets",
        "//software/thunderscope/gl/widgets/toolbar_icons/sandbox_mode:icon_loader",
    ],
)

py_library(
    name = "gl_gamecontroller_toolbar",
    srcs = ["gl_gamecontroller_toolbar.py"],
    deps = [
        ":gl_toolbar",
        "//proto:import_all_protos",
        "//software/networking:ssl_proto_communication",
        "//software/thunderscope/binary_context_managers:game_controller",
        "//software/thunderscope/common:common_widgets",
        "//software/thunderscope/gl/widgets/toolbar_icons/gamecontroller:icon_loader",
    ],
)
