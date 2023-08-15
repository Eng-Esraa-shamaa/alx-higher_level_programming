#!/usr/bin/python3
"""
function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file
    Args:
        filename: name of file
        text: the text to be inserted
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
