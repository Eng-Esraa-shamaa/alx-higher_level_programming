#!/usr/bin/python3
"""
function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Return:
        true or false
    Args:
        obj: the object to test
        a_class: the class to compare
    """
    if (issubclass(type(obj), a_class)) and type(obj) != a_class:
        return True
    return False
