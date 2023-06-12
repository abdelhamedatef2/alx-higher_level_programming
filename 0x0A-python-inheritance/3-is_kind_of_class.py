#!/usr/bin/python3
"""define class and inherited class function."""


def is_kind_of_class(obj, a_class):
    """Check if obj is inherited instance of class.

    Args:
        obj (any): obj to check.
        a_class (type): class to match type of obj to.

    Returns:
        If obj is inherited instance of class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
