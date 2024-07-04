#pragma once

#include <g3sinks/LogRotate.h>
#include <g3sinks/LogRotateWithFilter.h>

#include <g3log/g3log.hpp>
#include <g3log/loglevels.hpp>
#include <g3log/logmessage.hpp>
#include <g3log/logworker.hpp>

#include "google/protobuf/text_format.h"
#include "software/logger/custom_logging_levels.h"

// This undefines LOG macro defined by g3log
#undef LOG

// These macros allows us to overload arguments.
// https://stackoverflow.com/questions/11761703/overloading-macro-on-number-of-arguments
#define LOG_SELECT(_1, _2, NAME, ...) NAME
#define LOG(...) LOG_SELECT(__VA_ARGS__, LOG_2, LOG_1)(__VA_ARGS__)

// Called when LOG() is called with 1 argument. This is a copy of g3log's LOG() macro
// Note: curly braces are not used as we need to pipe log messages to the logger
#define LOG_1(level)                                                                     \
    if (!g3::logLevel(level))                                                            \
    {                                                                                    \
    }                                                                                    \
    else                                                                                 \
        INTERNAL_LOG_MESSAGE(level).stream()

// Called when LOG() is called with 2 arguments
#define LOG_2(level, filename)                                                           \
    if (level != CSV && level != VISUALIZE)                                              \
    {                                                                                    \
    }                                                                                    \
    else                                                                                 \
        LOG_1(level) << filename

std::ostream& operator<<(std::ostream& os, const google::protobuf::Message& message);
