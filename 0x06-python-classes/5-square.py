#!/usr/bin/python3
"""class Square that defines a square
"""


class Square:
    """definning sqaure
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        area = self.__size * self.__size
        return (area)

    def my_print(self):
        for row in range(0, self.__size):
            for col in range(0, self.__size):
                print("#", end="")
            print()
        if self.__size is 0:
            print()
