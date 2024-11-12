package(default_visibility = ["//visibility:public"])

load("@com_google_protobuf//:protobuf.bzl", "py_proto_library")
load("@rules_python//python:defs.bzl", "py_binary")

py_proto_library(
    name = "person_proto",
    srcs = [
        "person.proto",
    ]
)

# main file entry
py_binary(
    name = "main",
    srcs = ["main.py"], 
    deps = [
        ":person_proto"
    ]
)
