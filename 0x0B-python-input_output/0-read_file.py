#!/usr/bin/python3
"""defination of text file-reading function"""


def read_file(filename=""):
    """Reads text file then print it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
