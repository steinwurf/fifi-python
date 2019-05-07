// Copyright Steinwurf ApS 2011-2014.
// Distributed under the "STEINWURF EVALUATION LICENSE 1.0".
// See accompanying file LICENSE.rst or
// http://www.steinwurf.com/licensing

#pragma once

#include <pybind11/pybind11.h>

#include <string>

#include <fifi/fifi_utils.hpp>

#include "finite_field.hpp"

namespace fifi_python
{
template<class Field>
typename Field::value_type get_value(const std::string& elements, uint8_t index)
{
    return fifi::get_value<Field>((const uint8_t*)elements.c_str(), index);
}

template<class Field>
pybind11::bytes set_value(const std::string& elements, uint8_t index,
                    typename Field::value_type value)
{
    std::string elements_copy = elements;
    fifi::set_value<Field>((uint8_t*)elements_copy.c_str(), index, value);

    return pybind11::bytes(elements_copy);
}

template<class Field>
void fifi_utils(pybind11::module& m, const std::string& field)
{
    using namespace pybind11;

    m.def((field + std::string("_elements_to_length")).c_str(),
        &fifi::elements_to_length<Field>,
        arg("elements"),
        "Returns the number of value_type elements needed to store a "
        "certain number of field elements.\n\n"
        "elemenets.\n\n"
        "\t:param elements: The number of elements.\n"
        "\t:returns: The number of value_type elements needed.\n");
    m.def((field + std::string("_elements_to_size")).c_str(),
        &fifi::elements_to_size<Field>,
        arg("elements"),
        "Returns the minimum size in bytes required to accommodate a "
        "certain number of field elements.\n\n"
        "\t:param elements: the number of field elements.\n"
        "\t:return the size in bytes needed to store the field "
        "elements.\n");
    m.def((field + std::string("_size_to_length")).c_str(),
        &fifi::size_to_length<Field>, arg("bytes"),
        "Returns the number of value_type elements needed to store "
        "a certain number of bytes.\n\n"
        "\t:param bytes: the number of bytes to store.\n"
        "\t:return the number of value_type elements that need to be "
        "stored.\n");
    m.def((field + std::string("_length_to_size")).c_str(),
        &fifi::length_to_size<Field>, arg("length"),
        "Returns the size in bytes needed to store a certain "
        "number of value_type elements.\n\n"
        "\t:param length: the number of value_type elements to store.\n"
        "\t:return the size in bytes needed to store the value_type "
        "elements.\n");
    m.def((field + std::string("_length_to_elements")).c_str(),
        &fifi::length_to_elements<Field>,
        arg("length"),
        "Returns the number of field elements needed to store a certain "
        "number of value_type elements.\n\n"
        "\t:param length: the number of value_type elements.\n"
        "\t:return the number of field elements needed.\n");
    m.def((field + std::string("_size_to_elements")).c_str(),
        &fifi::size_to_elements<Field>, arg("bytes"),
        "Returns the number of field elements that can fit within a "
        "certain number of bytes.\n\n"
        "\t:param bytes: the number of bytes to store the field elements.\n"
        "\t:return the number of field elements stored within the bytes.\n");
    m.def((field + std::string("_get_value")).c_str(),
        &get_value<Field>,
        arg("elements"), arg("index"),
        "Useful abstraction functions for accessing field elements in a "
        "buffer. Note this function assumes that values are packed.\n\n"
        "\t:param elements: elements to get value from.\n"
        "\t:param index: index of element to access in the packed buffer.\n"
        "\t:return: the value of the element at specified index.\n");
    m.def((field + std::string("_set_value")).c_str(),
        &set_value<Field>,
        arg("elements"), arg("index"), arg("value"),
        "Useful abstraction function for assigning field elements in a "
        "buffer a specific value. Note this function assumes that values "
        "are packed.\n\n"
        "\t:param elements: elements to manipulate.\n"
        "\t:param index: index of element.\n"
        "\t:param value: value to assign element.\n"
        "\t:return: The modified buffer.\n");
    m.def((field + std::string("_pack_constant")).c_str(),
        &fifi::pack_constant<Field>, arg("constant"),
        "Helper function for creating packed constants. In Fifi we refer "
        "to values as packed if they utilize the entire underlying data "
        "type. As an example binary4 uses four bits for every field "
        "element but since no 4-bit data types are available we store it's "
        "value in an uint8_t. When using APIs requiring packed data we "
        "therefore have to pack the constant which ensures that both the "
        "high an low 4 bits have the right constant value (in the case of "
        "binary4).\n\n"
        "\t:param constant: The constant to pack.\n"
        "\t:return: The packed constant.\n"
       );
}
}
