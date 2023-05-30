#!/usr/bin/python3
"""Defines Square calss"""


class Square:
    """implement square."""

    def __init__(self, size=0):
        """Initialization of new Square.

        Args:
            size (int): size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size should be int")
        elif size < 0:
            raise ValueError("size should be >= 0")
        self.__size = size
