#!/usr/bin/python3
"""super class Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square."""

    def __init__(self, size):
        """
        Args:
            size: size of square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of square"""
        return (self.__size * self.__size)

    def __str__(self):
        """string representation of square"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
