#! /usr/bin/env python
# encoding: utf-8

# Copyright Steinwurf ApS 2011-2013.
# Distributed under the "STEINWURF EVALUATION LICENSE 1.0".
# See accompanying file LICENSE.rst or
# http://www.steinwurf.com/licensing

import fifi


def main():
    field = fifi.simple_online_binary4()
    a = 13
    b = 7

    print("{a} + {b} = {result}".format(a=a, b=b, result=field.add(a, b)))
    print("{a} - {b} = {result}".format(a=a, b=b, result=field.subtract(a, b)))
    print("{a} * {b} = {result}".format(a=a, b=b, result=field.multiply(a, b)))
    print("{a} / {b} = {result}".format(a=a, b=b, result=field.divide(a, b)))
    print("~{a} = {result}".format(a=a, result=field.invert(a)))

if __name__ == '__main__':
    main()
