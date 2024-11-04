#!/usr/bin/python3
"""UTF-8 validation module.
"""

def validUTF8(data):
# The line `"""Checks if a list of integers are valid UTF-8 codes."""` is a docstring in Python. Docstrings are used to provide documentation for functions, classes, or modules. In this case, the docstring is providing a brief description of the purpose of the `validUTF8` function, which is to check if a list of integers represents valid UTF-8 codes. This description helps other developers understand the function's intended use and behavior.
    """Checks if a list of integers are valid UTF-8 codes.
    """
    skip = 0
    n = len(data)
    for i in range(n):
        if skip > 0:
            skip -= 1
            continue
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            skip = 0
        elif data[i] & 0b11111000 == 0b11110000:
            # 4-byte utf-8 character encoding
            span = 4
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            # 3-byte utf-8 character encoding
            span = 3
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            # 2-byte utf-8 character encoding
            span = 2
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        else:
            return False
    return True
