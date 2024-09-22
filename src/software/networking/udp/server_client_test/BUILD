package(default_visibility = ["//visibility:public"])

# py_binary(
#     name = "udp_network_test_python", 
#     srcs = ["udp_network_test_python.py"], 
#     data = [
#         "//software:py_constants",
#         "//software:python_bindings",
#     ],
#     deps = [
#         #"//software:conftest",
#         "//proto:import_all_protos",
#     ]
#)

py_binary(
    name="test_client", 
    srcs = [
        "test_client.py",
    ], 
    data = [
        "//software:py_constants",
        "//software:python_bindings",
    ],
    deps = [
        "//proto:import_all_protos",
    ]
)

cc_binary(
    name = "test_server",
    srcs = [
        "test_server.cpp",
    ], 
    deps = [ 
        "//software/networking/udp:threaded_proto_udp_sender",
        "//proto:tbots_cc_proto"
    ]
)
