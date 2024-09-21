# thank you so much!: https://github.com/google/re2/blob/108914d28a79243d4300e7e651cd0a0d5883ca0f/python/setup.py
# github issue: https://github.com/pybind/pybind11_bazel/issues/78
# for this person who figured it out! 
# python toolchains stuff: 

load("@rules_python//python/cc:py_cc_toolchain.bzl", "py_cc_toolchain")
load("@rules_python//python:py_runtime.bzl", "py_runtime")
load("@rules_python//python:py_runtime_pair.bzl", "py_runtime_pair")

package(default_visibility = ["//visibility:public"])

toolchain(
    name = "py",
    toolchain = ":py_toolchain",
    toolchain_type = "@rules_python//python:toolchain_type",
)

py_runtime_pair(
    name = "py_toolchain",
    py3_runtime = ":interpreter",
)

py_runtime(
    name = "interpreter",
    interpreter_path = "C:/Users/Vince/AppData/Local/Programs/Python/Python311/python.exe",
    interpreter_version_info = {
        "major": "3",
        "minor": "11",
    },
    python_version = "PY3",
)

toolchain(
    name = "py_cc",
    toolchain = ":py_cc_toolchain",
    toolchain_type = "@rules_python//python/cc:toolchain_type",
)

py_cc_toolchain(
    name = "py_cc_toolchain",
    headers = ":headers",
    libs = ":libraries",
    python_version = "3.11",
)

cc_library(
    name = "headers",
    hdrs = glob(["include/**/*.h"]),
    includes = ["include"],
    deps = select({
        "@platforms//os:windows": [":interface_library"],
        "//conditions:default": [],
    }),
)

cc_import(
    name = "interface_library",
    interface_library = select({
        "@platforms//os:windows": "libs/python311.lib",
        "//conditions:default": None,
    }),
    system_provided = True,
)

# Not actually necessary for our purposes. :)
cc_library(
    name = "libraries",
)
