#!/usr/bin/python3
"""Define child list class MyList."""


class MyList(list):
    """this class is child of built-in list class."""

    def print_sorted(self):
        """That prints sorted list in ascending order."""
        print(sorted(self))
