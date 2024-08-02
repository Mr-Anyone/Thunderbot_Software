#pragma once

#include <string>
#include <memory>

/**
 * Demangles typeid name
 *
 * @param mangled_name The mangled name to demangle
 *
 * @return the demangled string representation
 */
std::string demangleTypeId(const char* mangled_name);

/**
 * Gets the demangled typeid name of an object reference
 *
 * Note: This does not work on classes; instead use TYPENAME
 *
 * Note: Setting up the arguments as const reference avoids evaluating expressions with
 * side effects as operand to typeid
 * https://stackoverflow.com/questions/46494928/clang-warning-on-expression-side-effects
 *
 * @param obj_ref The reference to the object
 *
 * @return the demangled string representation
 */
template <typename T>
std::string objectTypeName(const T& obj_ref)
{
    // I think this would work in MSVC!
    return std::string {typeid(T).name()};

//     // stackover: https://stackoverflow.com/questions/81870/is-it-possible-to-print-a-variables-type-in-standard-c
// #ifdef __clang__
//     std::string p = __PRETTY_FUNCTION__;
//     return std::string(p.data() + 34, p.size() - 34 - 1);
// #elif defined(__GNUC__)
//     std::string p = __PRETTY_FUNCTION__;
// #  if __cplusplus < 201402
//     return std::string(p.data() + 36, p.size() - 36 - 1);
// #  else
//     return std::string(p.data() + 49, p.find(';', 49) - 49);
// #  endif
// #elif defined(_MSC_VER)
//     std::string p = __FUNCSIG__;
//     return std::string(p.data() + 84, p.size() - 84 - 7);
// #endif
}

/**
 * MACRO to get typename of the object, i.e.
 * ```
 * ClassA object_a;
 * TYPENAME(object_a); // returns ClassA
 * ```
 *
 * @param object The object to get typename for
 *
 * @return the string representation of the object
 */
// #define TYPENAME(object) (demangleTypeId(typeid(object).name()))
