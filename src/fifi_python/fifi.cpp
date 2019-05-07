// Copyright Steinwurf ApS 2011-2013.
// Distributed under the "STEINWURF EVALUATION LICENSE 1.0".
// See accompanying file LICENSE.rst or
// http://www.steinwurf.com/licensing

#include <pybind11/pybind11.h>

#include <fifi/binary.hpp>
#include <fifi/binary4.hpp>
#include <fifi/binary8.hpp>
#include <fifi/binary16.hpp>

#include <fifi/extended_log_table.hpp>
#include <fifi/full_table.hpp>
#include <fifi/log_table.hpp>
#include <fifi/optimal_prime.hpp>
#include <fifi/simple_online.hpp>

#include "finite_field.hpp"
#include "fifi_utils.hpp"

namespace fifi_python
{
std::string version()
{
    std::string version = std::string("fifi-python: ");
    version += STEINWURF_FIFI_PYTHON_VERSION;

    // Add dependency versions:
    version += std::string("\n\tallocate: ");
#ifdef STEINWURF_ALLOCATE_VERSION
    version += std::string(STEINWURF_ALLOCATE_VERSION);
#endif
    version += std::string("\n\tcpuid: ");
#ifdef STEINWURF_CPUID_VERSION
    version += std::string(STEINWURF_CPUID_VERSION);
#endif
    version += std::string("\n\tfifi: ");
#ifdef STEINWURF_FIFI_VERSION
    version += std::string(STEINWURF_FIFI_VERSION);
#endif
    version += std::string("\n\tplatform: ");
#ifdef STEINWURF_PLATFORM_VERSION
    version += std::string(STEINWURF_PLATFORM_VERSION);
#endif
    version += std::string("\n\tpybind11: ");
#ifdef STEINWURF_PYBIND11_VERSION
    version += std::string(STEINWURF_PYBIND11_VERSION);
#endif
    version += std::string("\n\tstorage: ");
#ifdef STEINWURF_STORAGE_VERSION
    version += std::string(STEINWURF_STORAGE_VERSION);
#endif

    return version;
}

PYBIND11_MODULE(fifi, m)
{
    pybind11::options options;
    options.disable_function_signatures();

    m.attr("__version__") = version();

    using namespace fifi;

    finite_field<extended_log_table, binary16>(
        m, "extended_log_table", "binary16");
    finite_field<extended_log_table, binary4>(
        m, "extended_log_table", "binary4");
    finite_field<extended_log_table, binary8>(
        m, "extended_log_table", "binary8");

    finite_field<full_table, binary4>(m, "full_table", "binary4");
    finite_field<full_table, binary8>(m, "full_table", "binary8");

    finite_field<log_table, binary4>(m, "log_table", "binary4");
    finite_field<log_table, binary8>(m, "log_table", "binary8");
    finite_field<log_table, binary16>(m, "log_table", "binary16");

    finite_field<optimal_prime, prime2325>(m, "optimal_prime", "prime2325");

    finite_field<simple_online, binary>(m, "simple_online", "binary");
    finite_field<simple_online, binary4>(m, "simple_online", "binary4");
    finite_field<simple_online, binary8>(m, "simple_online", "binary8");
    finite_field<simple_online, binary16>(m, "simple_online", "binary16");

    fifi_utils<binary>(m, "binary");
    fifi_utils<binary4>(m, "binary4");
    fifi_utils<binary8>(m, "binary8");
    fifi_utils<binary16>(m, "binary16");
    fifi_utils<prime2325>(m, "prime2325");
}
}
