#!/usr/bin/python3
"""defination of square based on 2-square.py"""


class Square:
    """define square by it's size"""
    def __init__(self, size=0):
        """initialization of  size arg"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size should be int')

        if size < 0:
            raise ValueError('size should be >= 0')

    def area(self):
        """returns square's area"""
        area = self.__size * self.__size
        return area
