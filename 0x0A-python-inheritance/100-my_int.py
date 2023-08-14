#!/usr/bin/python3
"""
defining class MyInt that inherits from int
"""


class MyInt(int):
    """
    class MyInt
    """
    def __eq__(self, value):
        """function which is opposie of != behavior."""
        return self.real != value

    def __ne__(self, value):
        """function with the oposite of  == behavior."""
        return self.real == value
