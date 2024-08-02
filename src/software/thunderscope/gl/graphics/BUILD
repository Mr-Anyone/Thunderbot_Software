package(default_visibility = ["//visibility:public"])


py_library(
    name = "gl_circle",
    srcs = ["gl_circle.py"],
    deps = [
        ":gl_shape",
    ],
)

py_library(
    name = "gl_rect",
    srcs = ["gl_rect.py"],
    deps = [
        ":gl_shape",
    ],
)

py_library(
    name = "gl_robot_outline",
    srcs = ["gl_robot_outline.py"],
    deps = [
        ":gl_shape",
        "//software/thunderscope/gl/helpers:triangulate",
    ],
)

py_library(
    name = "gl_robot",
    srcs = ["gl_robot.py"],
    deps = [
        ":gl_robot_outline",
    ],
)

py_library(
    name = "gl_sphere",
    srcs = ["gl_sphere.py"],
    deps = [
    ],
)

py_library(
    name = "gl_goal",
    srcs = ["gl_goal.py"],
    deps = [
    ],
)

py_library(
    name = "gl_polygon",
    srcs = ["gl_polygon.py"],
    deps = [
        ":gl_shape",
        "//software/thunderscope/gl/helpers:triangulate",
    ],
)

py_library(
    name = "gl_shape",
    srcs = ["gl_shape.py"],
    deps = [
    ],
)

py_library(
    name = "gl_heatmap",
    srcs = ["gl_heatmap.py"],
    deps = [
    ],
)

py_library(
    name = "gl_painter",
    srcs = ["gl_painter.py"],
    deps = [
    ],
)

py_library(
    name = "gl_gradient_legend",
    srcs = ["gl_gradient_legend.py"],
    deps = [
        ":gl_painter",
    ],
)

py_library(
    name = "gl_stadium",
    srcs = ["gl_stadium.py"],
    deps = [
        ":gl_shape",
    ],
)
