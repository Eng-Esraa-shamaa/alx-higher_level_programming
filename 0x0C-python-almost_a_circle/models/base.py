#!/usr/bin/python3
"""
definning class base
"""


class Base:
    """
    base class
    private class attributes:
        __nb_objects: number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            id: id of new base
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
