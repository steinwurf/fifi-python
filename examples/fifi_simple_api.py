#! /usr/bin/env python
# encoding: utf-8

# Copyright Steinwurf ApS 2011-2013.
# Distributed under the "STEINWURF EVALUATION LICENSE 1.0".
# See accompanying file LICENSE.rst or
# http://www.steinwurf.com/licensing

from fifi import *


simple_api_template = """
class {classname}(object):
    \"\"\"Finite field number class for {name}.\"\"\"
    range = range(2**{degree})
    field = {implementation}_{name}()
    def __init__(self, number):
        super({classname}, self).__init__()
        assert number < 2**{degree}, \\
            "{{}} is out of range for {name}.".format(number)
        self.number = number

    def __convert(self, b):
        if type(b) is int:
            return {classname}(b)
        return b

    def __add__(self, b):
        b = self.__convert(b)
        return {classname}({classname}.field.add(self.number, b.number))

    def __radd__(self, b):
        b = self.__convert(b)
        return {classname}({classname}.field.add(b.number, self.number))

    def __sub__(self, b):
        b = self.__convert(b)
        return {classname}({classname}.field.subtract(self.number, b.number))

    def __rsub__(self, b):
        b = self.__convert(b)
        return {classname}({classname}.field.subtract(b.number, self.number))

    def __mul__(self, b):
        b = self.__convert(b)
        return {classname}({classname}.field.multiply(self.number, b.number))

    def __rmul__(self, b):
        b = self.__convert(b)
        return {classname}({classname}.field.multiply(b.number, self.number))

    def __div__(self, b):
        b = self.__convert(b)
        return {classname}({classname}.field.divide(self.number, b.number))

    def __rdiv__(self, b):
        b = self.__convert(b)
        return {classname}({classname}.field.divide(b.number, self.number))

    def __truediv__(self, b):
        return self.__div__(b)

    def __rtruediv__(self, b):
        b = self.__convert(b)
        return b.__div__(self)

    def __invert__(self):
        return {classname}({classname}.field.invert(self.number))

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, b):
        return self.number == b.number

    def __ne__(self, b):
        return self.number != b.number

    def __gt__(self, b):
        return self.number > b.number

    def __lt__(self, b):
        return self.number < b.number

    def __ge__(self, b):
        return self.number >= b.number

    def __le__(self, b):
        return self.number <= b.number
"""

fields = {
    'binary': {
        'classname': 'B',
        'degree': 1
    },
    'binary4': {
        'classname': 'B4',
        'degree': 4
    },
    'binary8': {
        'classname': 'B8',
        'degree': 8
    },
    'binary16': {
        'classname': 'B16',
        'degree': 16
    },
}

for name, field in fields.items():
    exec(simple_api_template.format(
        name=name,
        implementation='simple_online',
        **field))
