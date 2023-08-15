#!/usr/bin/python3
"""
returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    function returns the dictionary description with simple data structure
    Args:
        obj: the object
    """
    return obj.__dict__
