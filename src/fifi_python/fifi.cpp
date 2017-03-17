// Copyright Steinwurf ApS 2011-2013.
// Distributed under the "STEINWURF RESEARCH LICENSE 1.0".
// See accompanying file LICENSE.rst or
// http://www.steinwurf.com/licensing

#include <boost/python.hpp>

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
    version += std::string("\n\tboost: ");
#ifdef STEINWURF_BOOST_VERSION
    version += std::string(STEINWURF_BOOST_VERSION);
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
    version += std::string("\n\tstorage: ");
#ifdef STEINWURF_STORAGE_VERSION
    version += std::string(STEINWURF_STORAGE_VERSION);
#endif

    return version;
}

void create_version_function()
{
    using namespace boost::python;
    scope().attr("__version__") = version();
}


BOOST_PYTHON_MODULE(fifi)
{
    using namespace fifi;

    boost::python::docstring_options doc_options;
    doc_options.disable_signatures();

    create_version_function();

    finite_field<extended_log_table, binary16>(
        "extended_log_table", "binary16");
    finite_field<extended_log_table, binary4>(
        "extended_log_table", "binary4");
    finite_field<extended_log_table, binary8>(
        "extended_log_table", "binary8");

    finite_field<full_table, binary4>("full_table", "binary4");
    finite_field<full_table, binary8>("full_table", "binary8");

    finite_field<log_table, binary16>("log_table", "binary16");
    finite_field<log_table, binary4>("log_table", "binary4");
    finite_field<log_table, binary8>("log_table", "binary8");

    finite_field<optimal_prime, prime2325>("optimal_prime", "prime2325");

    finite_field<simple_online, binary16>("simple_online", "binary16");
    finite_field<simple_online, binary4>("simple_online", "binary4");
    finite_field<simple_online, binary8>("simple_online", "binary8");
    finite_field<simple_online, binary>("simple_online", "binary");

    fifi_utils<binary>("binary");
    fifi_utils<binary4>("binary4");
    fifi_utils<binary8>("binary8");
    fifi_utils<binary16>("binary16");
    fifi_utils<prime2325>("prime2325");
}
}
