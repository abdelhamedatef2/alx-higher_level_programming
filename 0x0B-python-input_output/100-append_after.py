#!/usr/bin/python3
"""defination of text file insert function."""


def append_after(filename="", search_string="", new_string=""):
    """insert text after each line containing specific str in file.
    Args:
        filename (str): name of file.
        search_string (str): str to search for within file.
        new_string (str): str to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
