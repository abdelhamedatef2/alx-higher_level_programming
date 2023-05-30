#!/usr/bin/python3
"""defination of class square"""


class Square:
    """initialization of size as an arg"""
    def __init__(self, size=0):
        """initialization of new square with size arg"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size should be int')
        if size < 0:
            raise ValueError('size should be >= 0')
