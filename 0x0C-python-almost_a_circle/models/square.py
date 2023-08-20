#!/usr/bin/python3
"""
defining square model
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defining square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size: size of square.
            x: the x coordiante.
            y: the y coordiante.
            id: id of new square.
        """
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """
        prints the string representation of the square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.__x,
                                                 self.__y,
                                                 self.__width)

    @property
    def size(self):
        """defining size of square"""
        return self.__width

    @size.setter
    def size(self, value):
        """getter/setter of size of square"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value

    @property
    def x(self):
        """
        the x coordiante
        """
        return self.__x

    @x.setter
    def x(self, x):
        """getter/setter of x coordiantes"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """the y coordinates"""
        return self.__y

    @y.setter
    def y(self, y):
        """getter/setter of the y coordinates"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """it returns the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
