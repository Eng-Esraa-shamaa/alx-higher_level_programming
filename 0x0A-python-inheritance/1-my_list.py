#!/usr/bin/python3
"""
class MyList that inherits list
"""


class MyList(list):
    """
    Public instance method that prints the list
    """
    def print_sorted(self):
        """prints the list but sorted (ascending sort)"""
        list_ = self[:]
        list_.sort()
        print(list_)
