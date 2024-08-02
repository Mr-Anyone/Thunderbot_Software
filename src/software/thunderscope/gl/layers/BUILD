package(default_visibility = ["//visibility:public"])


py_library(
    name = "gl_layer",
    srcs = ["gl_layer.py"],
    deps = [
        "//software/thunderscope:thread_safe_buffer",
        "//software/thunderscope/gl/helpers:extended_gl_view_widget",
        "//software/thunderscope/gl/helpers:observable_list",
    ],
)

py_library(
    name = "gl_path_layer",
    srcs = ["gl_path_layer.py"],
    deps = [
        ":gl_layer",
        "//software/thunderscope/gl/graphics:gl_polygon",
        "//software/thunderscope/gl/graphics:gl_robot_outline",
    ],
)

py_library(
    name = "gl_obstacle_layer",
    srcs = ["gl_obstacle_layer.py"],
    deps = [
        ":gl_layer",
        "//software/thunderscope/gl/graphics:gl_circle",
        "//software/thunderscope/gl/graphics:gl_polygon",
        "//software/thunderscope/gl/graphics:gl_stadium",
    ],
)

py_library(
    name = "gl_debug_shapes_layer",
    srcs = ["gl_debug_shapes_layer.py"],
    deps = [
        ":gl_layer",
        "//software/thunderscope/gl/graphics:gl_circle",
        "//software/thunderscope/gl/graphics:gl_polygon",
        "//software/thunderscope/gl/graphics:gl_stadium",
    ],
)

py_library(
    name = "gl_passing_layer",
    srcs = ["gl_passing_layer.py"],
    deps = [
        ":gl_layer",
        "//software/thunderscope/gl/graphics:gl_polygon",
    ],
)

py_library(
    name = "gl_attacker_layer",
    srcs = ["gl_attacker_layer.py"],
    deps = [
        ":gl_layer",
        "//software/thunderscope/gl/graphics:gl_circle",
        "//software/thunderscope/gl/graphics:gl_polygon",
    ],
)

py_library(
    name = "gl_world_layer",
    srcs = ["gl_world_layer.py"],
    deps = [
        ":gl_layer",
        "//software/thunderscope:proto_unix_io",
        "//software/thunderscope/gl/graphics:gl_circle",
        "//software/thunderscope/gl/graphics:gl_goal",
        "//software/thunderscope/gl/graphics:gl_polygon",
        "//software/thunderscope/gl/graphics:gl_rect",
        "//software/thunderscope/gl/graphics:gl_robot",
        "//software/thunderscope/gl/graphics:gl_sphere",
    ],
)

py_library(
    name = "gl_sandbox_world_layer",
    srcs = ["gl_sandbox_world_layer.py"],
    deps = [
        ":gl_world_layer",
    ],
)

py_library(
    name = "gl_simulator_layer",
    srcs = ["gl_simulator_layer.py"],
    deps = [
        ":gl_layer",
        "//software/thunderscope/gl/graphics:gl_sphere",
    ],
)

py_library(
    name = "gl_tactic_layer",
    srcs = ["gl_tactic_layer.py"],
    deps = [
        ":gl_layer",
    ],
)

py_library(
    name = "gl_validation_layer",
    srcs = ["gl_validation_layer.py"],
    deps = [
        ":gl_layer",
        "//software/thunderscope/gl/graphics:gl_circle",
        "//software/thunderscope/gl/graphics:gl_painter",
        "//software/thunderscope/gl/graphics:gl_polygon",
    ],
)

py_library(
    name = "gl_measure_layer",
    srcs = ["gl_measure_layer.py"],
    deps = [
        ":gl_layer",
        "//software/thunderscope/gl/graphics:gl_polygon",
        "//software/thunderscope/gl/graphics:gl_sphere",
    ],
)

py_library(
    name = "gl_cost_vis_layer",
    srcs = ["gl_cost_vis_layer.py"],
    deps = [
        ":gl_layer",
        "//software/thunderscope/gl/graphics:gl_gradient_legend",
        "//software/thunderscope/gl/graphics:gl_heatmap",
    ],
)

py_library(
    name = "gl_trail_layer",
    srcs = ["gl_trail_layer.py"],
    deps = [
        ":gl_layer",
        "//software/thunderscope/gl/graphics:gl_polygon",
    ],
)
