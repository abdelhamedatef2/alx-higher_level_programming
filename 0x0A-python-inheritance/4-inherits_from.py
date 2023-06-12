#!/usr/bin/python3
"""defines inherited class function."""


def inherits_from(obj, a_class):
    """checks if obj is inherited instance of class.
    Args:
        obj (any): obj to check.
        a_class (type): class to match type of obj to.
    Returns:
        If obj inherited instance of class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
