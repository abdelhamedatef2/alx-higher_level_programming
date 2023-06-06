#!/usr/bin/python3

"""Module used to find max int in list"""

def max_integer(list=[]):
    """Function that used to find and return max int in a list.
    If list empty,function returns void.
    Args:
        list (list): List of ints.
    Returns:
        int or None: Max int in the list,None if list empty.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
