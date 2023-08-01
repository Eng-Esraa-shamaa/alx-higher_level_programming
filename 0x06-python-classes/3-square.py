#!/usr/bin/python3
"""class Square that defines a square
"""


class Square:
    """defining class square
    """
    def __init__(self, size=0):
        """size of square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """area of square
        """
        area = self.__size * self.__size
        return (area)
