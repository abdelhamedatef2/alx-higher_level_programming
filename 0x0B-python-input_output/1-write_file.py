#!/usr/bin/python3
"""defination of file-writing function."""


def write_file(filename="", text=""):
    """write str to UTF8 text file.
    Args:
        filename (str): name of file to write.
        text (str): text to write to file.
    Returns:
        returns num of chars written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
