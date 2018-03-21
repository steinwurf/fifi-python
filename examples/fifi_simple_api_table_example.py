#! /usr/bin/env python
# encoding: utf-8

# Copyright Steinwurf ApS 2011-2013.
# Distributed under the "STEINWURF EVALUATION LICENSE 1.0".
# See accompanying file LICENSE.rst or
# http://www.steinwurf.com/licensing

from fifi_simple_api import B4


def print_finite_field_table(b, operation):
    """
    Prints a table using the simple fifi api. Note printing a table for B16
    consumes a huge amount of memory and will probably not work.
    """
    # Create the string as a list to improve performance of concatenations.
    string = []
    range = b.range

    min_digits = 3
    digits = max(min_digits, len(str(range[-1])))
    cell = "{0:>%ss}" % (digits + 1)
    column_label = "{0:>%ss}|" % (digits)

    string.append(' '*(digits))
    string.append("|")
    for i in range:
        string.append(cell.format(str(i)))
    string.append("\n")
    string.append('-'*(digits))
    string.append('+')
    string.append('-'*((digits+1) * len(range)))
    string.append("\n")

    for i in range:
        string.append((column_label).format(str(i)))
        for j in range:
            string.append(cell.format(str(operation(b(i), b(j)))))
        string.append("\n")

    return ''.join(string)


def main():
    field = B4

    print('addition')
    print(print_finite_field_table(field, lambda a, b: a + b))

    print('subtraction')
    print(print_finite_field_table(field, lambda a, b: a - b))

    print('multiplication')
    print(print_finite_field_table(field, lambda a, b: a * b))

    print('division')
    print(print_finite_field_table(
        field,
        lambda a, b: a / b if b.number != 0 else 'NAN'))

    print('invert')
    print('------')
    for i in field.range:
        if i == 0:
            continue
        print('{0:>2s}|{1:>3s}'.format(str(i), str(~field(i))))

if __name__ == '__main__':
    main()
