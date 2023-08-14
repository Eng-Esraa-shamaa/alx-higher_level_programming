#!/usr/bin/python3
"""
function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, attr, value):
    """
    Args:
        obj: the object
        attr: the attribute to be added
        value: value of attr
    Raises:
        typeError: when adding new attr
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
