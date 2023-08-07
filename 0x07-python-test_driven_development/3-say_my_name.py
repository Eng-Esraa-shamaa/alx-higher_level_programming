#!/usr/bin/python3
"""
module: say_my_name
"""


def say_my_name(first_name, last_name=''):
    """ print first and last name
    Args:
        first_name: The first name to print.
        last_name: The last name to print.
    Raises:
        TypeError: if first_name or last_name are not strings.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
