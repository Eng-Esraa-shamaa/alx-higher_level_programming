#!/usr/bin/python3
"""
function adds two integers
returns sum of two integers
the floats converted into int
"""


def add_integer(a, b=98):
    """add_integer - return the sum of two integers
    Raises:
        TypeError if a or b are not and int or float"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
