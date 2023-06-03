#!/usr/bin/python3
"""
script defines function for printing square using (#) char.
"""


def print_square(size):
    """
    Print square with (#) char.

    Args:
        size (int): height/width of square.

    Raises:
        TypeError: If size not int.
        ValueError: If size is < 0
    """

    # Check if size int and not negative
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print square
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
