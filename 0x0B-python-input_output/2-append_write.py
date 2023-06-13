#!/usr/bin/python3
"""defination of file-appending function."""


def append_write(filename="", text=""):
    """appends str to end of UTF8 text file.
    Args:
        filename (str): name of the file to append to.
        text (str): string to append to the file.
    Returns:
        This is numb of chars appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
