#!/usr/bin/python3
"""
print_square module.
it has a function prints a square with #.
"""


def print_square(size):
    """
    Printing square
    Raises:
        TypeError: if size is not integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
