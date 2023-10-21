cc_library(
    name = "tracy",
    srcs = glob([
        "zstd/**/*.cpp",
        "public/tracy/common/*.cpp",
        "common/*.cpp",
        "public/tracy/client/*.cpp",
        "public/tracy/libbacktrace/*.cpp",
        "public/libbacktrace/*.cpp",
        "public/client/*.cpp",
        "public/common/*.cpp",
        "imgui/*.cpp",
        "tracy/*.cpp",
    ]),
    hdrs = ["public/tracy/Tracy.hpp"] + glob([
        "public/tracy/common/*.hpp",
        "public/tracy/common/*.h",
        "public/tracy/client/*.hpp",
        "profiler/**/*.hpp",
        "public/client/*.hpp",
        "public/client/*.h",
        "profiler/**/*.h",
        "zstd/**/*.h",
        "imgui/**/*.hpp",
        "imgui/**/*.h",
        "public/common/*.h",
        "public/common/*.hpp",
        "public/common/**/*.h",
        "public/common/**/*.hpp",
        "public/tracy/client/*.h",
        "public/tracy/*.h",
        "public/libbacktrace/*.hpp",
        "public/libbacktrace/*.h",
        "common/*.h",
        "common/*.hpp",
        "common/**/*.h",
        "common/**/*.hpp",
        "tracy/*.h",
    ]),
    #alwayslink = True,
    defines = [
        "TRACY_ENABLE",
    ],
    includes = [
        "/usr/include/capstone",
        "/usr/include/freetype2",
        "/usr/include/libpng16",
        "client",
        "common",
        "imgui",
        "profiler/src/imgui",
        "public",
        "public/client",
        "public/common",
        "public/libbacktrace",
        "public/tracy",
        "public/tracy/client",
    ],
    linkopts = ["-pthread -ldl"],
    linkstatic = True,
    textual_hdrs =
        [
            "public/common/tracy_lz4.cpp",
        ],
    visibility = ["//visibility:public"],
)