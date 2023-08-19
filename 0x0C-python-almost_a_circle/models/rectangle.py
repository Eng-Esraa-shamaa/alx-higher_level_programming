#!/usr/bin/python3
"""
defining class rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width: width of rectangle
            height: height of rectangle
            x: x coordinate of rectangle
            y: y coordinate of rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """defining property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """getter/setter of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """defining property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """getter/setter of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """deffining x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """getter/setter of x value"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """definning y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """getter/setter of y value"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of rectangle"""
        return (self.height * self.width)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for a in range(0, self.__y):
            print("")
        for i in range(0, self.__height):
            for b in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """prints the string representation of  Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        attrs = ["id", "width", "height", "x", "y"]
        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """it return dictionary representation rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
