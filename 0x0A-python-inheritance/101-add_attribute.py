#!/usr/bin/python3
"""Define function to adds attribute to obj."""


def add_attribute(obj, att, value):
    """adds new attribute to obj if possible.
    Args:
        obj (any): obj to add attr to.
        att (str): name of attr to add to obj.
        value (any): value of att.
    Raises:
        TypeError: If attr cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
