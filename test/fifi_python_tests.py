#! /usr/bin/env python
# encoding: utf-8

# Copyright Steinwurf ApS 2011-2013.
# Distributed under the "STEINWURF EVALUATION LICENSE 1.0".
# See accompanying file LICENSE.rst or
# http://www.steinwurf.com/licensing

import json
import os
import unittest
import struct

import fifi

DATA_FILE_NAME = 'data.json'


def read_json(file_path):
    """
    Reads a json file
    """
    with open(file_path) as data_file:
        return json.load(data_file)

# Get absolute path of the test data file
file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), DATA_FILE_NAME)

# Read test data
test_data = read_json(file_path)

# Store information about the fields:
# key: Name,
# implementations: Implementations for that specific field,
# value_type: Based on python struct Format Characters, more info here:
# https://docs.python.org/2/library/struct.html#byte-order-size-and-alignment
# is_exact: Specifies whether the underlying type is exact, meaning that the
# value type can contain exactly one element.
fields = {
    'binary': {
        'implementations': [
            fifi.simple_online_binary
        ],
        'value_type': 'B',
        'is_exact': False
    },
    'binary4': {
        'implementations': [
            fifi.extended_log_table_binary4,
            fifi.full_table_binary4,
            fifi.log_table_binary4,
            fifi.simple_online_binary4
        ],
        'value_type': 'B',
        'is_exact': False
    },
    'binary8': {
        'implementations': [
            fifi.extended_log_table_binary8,
            fifi.full_table_binary8,
            fifi.log_table_binary8,
            fifi.simple_online_binary8
        ],
        'value_type': 'B',
        'is_exact': True
    },
    'binary16': {
        'implementations': [
            fifi.extended_log_table_binary16,
            fifi.log_table_binary16,
            fifi.simple_online_binary16
        ],
        'value_type': 'H',
        'is_exact': True
    },
    'prime2325': {
        'implementations': [
            fifi.optimal_prime_prime2325
        ],
        'value_type': 'I',
        'is_exact': True
    }
}


class TestVersion(unittest.TestCase):

    def test_version(self):
        versions = fifi.__version__.split('\n')
        for version in versions:
            # Make sure that a version number is available for all
            # dependencies.
            self.assertNotEqual(
                version.split(':')[1].strip(), '', msg=version.strip())


class TestOperations(unittest.TestCase):

    def do_test(self, operation):
        for field in fields:
            for implementation in fields[field]['implementations']:
                finite_field = implementation()

                for d in test_data[field].get(operation) or []:
                    args = []
                    args.append(d['input1'])
                    if 'input2' in d:
                        args.append(d['input2'])
                    expected = d['result']
                    result = getattr(finite_field, operation)(*args)
                    self.assertEqual(result, expected)

    def test_add(self):
        self.do_test('add')

    def test_multiply(self):
        self.do_test('multiply')

    def test_divide(self):
        self.do_test('divide')

    def test_invert(self):
        self.do_test('invert')

    def test_packed_add(self):
        self.do_test('packed_add')

    def test_packed_multiply(self):
        self.do_test('packed_multiply')

    def test_packed_divide(self):
        self.do_test('packed_divide')

    def test_packed_invert(self):
        self.do_test('packed_invert')

    def do_region_test(self, operation):
        for field in fields:
            # This unit test in not able to pack the elements if they are not
            # exact.
            if not fields[field]['is_exact']:
                continue

            # "<" forces little endian (and thereby a standard byte size).
            # See "struct" documentation for more info.
            value_type = "<{}".format(fields[field]['value_type'])
            for implementation in fields[field]['implementations']:
                finite_field = implementation()

                input1 = bytes()
                input2 = bytes()
                expected = bytes()

                for d in test_data[field].get(operation) or []:
                    input1 += struct.pack(value_type, d['input1'])
                    if 'input2' in d:
                        input2 += struct.pack(value_type, d['input2'])
                    expected += struct.pack(value_type, d['result'])

                real_operation = "region_{}".format(operation)
                result = getattr(finite_field, real_operation)(input1, input2)
                self.assertEqual(result, expected)

    def test_region_add(self):
        self.do_region_test('add')

    def test_region_multiply(self):
        self.do_region_test('multiply')

    def test_region_divide(self):
        self.do_region_test('divide')


def main():
    unittest.main()

if __name__ == "__main__":
    main()
