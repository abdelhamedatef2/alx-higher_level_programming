#!/usr/bin/python3
"""
script that define function for int add.
"""


def add_integer(a, b=98):
    """
    function that returns int add of a and b.

    If a or b is non-int and non-float, TypeError is raised.
    Float args are typecasted.
    """

    # Check if a not int or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if b not int or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a,b to ints and return the sum
    return int(a) + int(b)
