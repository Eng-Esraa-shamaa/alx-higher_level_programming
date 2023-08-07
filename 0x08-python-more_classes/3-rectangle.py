#!/usr/bin/python3
"""
rectangle class
"""


class Rectangle:
    """
    class rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initializing width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter and setter of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter and setter of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        area of rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """
        print the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return("")

        rect = []
        for x in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if x != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
