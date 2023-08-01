#!/usr/bin/python3
"""class Square that defines a square
"""


class Square:
    """defining class square
    """
    def __init__(self, size=0, position=(0, 0)):
        """defining the square.

        Args:
            size (int): size square.
            position (int, int): position of square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set size of  square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the size of square
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Get/set size of square."""
        return(self.__position)

    @position.setter
    def position(self, value):
        """set the position of square
        """
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for num in value:
            if type(num) is not int or num < 0:
                raise TypeError('position must be a tuple of ' +
                                '2 positive integers')
        self.__position = value

    def area(self):
        """area of square
        """
        area = self.__size * self.__size
        return (area)

    def my_print(self):
        """print square
        """
        if self.__size == 0:
            print()
            return
        else:
            for v_position in range(0, self.__position[1]):
                print()
            for row in range(0, self.__size):
                for h_position in range(0, self.__position[0]):
                    print(" ", end="")
                for col in range(0, self.__size):
                    print("#", end="")
                print()
