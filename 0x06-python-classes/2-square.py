#!/usr/bin/python3
"""class Square that defines a square
"""


class Square:
    """defines square
    """
    def __init__(self, size = 0):
        if type(size) is not int:
            raise TypeError('size must be an intege')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
