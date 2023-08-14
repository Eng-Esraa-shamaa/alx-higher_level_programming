#!/usr/bin/python3
"""
function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    true if the object is instance of
    Args:
        obj: the object to test
        a_class: class to check in it
    """
    if isinstance(obj, a_class):
        return True
    return False
