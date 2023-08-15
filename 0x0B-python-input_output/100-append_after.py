#!/usr/bin/python3
"""
function that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Args:
        filename: name of file
        search_string: string to search for it
        new_string: new added string
    """
    search = ""
    with open(filename) as f:
        for line in f:
            search += line
            if search_string in line:
                search += new_string
    with open(filename, 'w') as m:
        m.write(search)
