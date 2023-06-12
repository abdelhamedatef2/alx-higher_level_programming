#!/usr/bin/python3
"""
Define class-checking function.
"""


def is_same_class(obj, a_class):
    """Check if object is an instance of given class.
    Args:
        obj (any): obj to check.
        a_class (type): class to match type of obj to.
    Returns:
        If obj is instance of class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
