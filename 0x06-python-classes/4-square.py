#!/usr/bin/python3
"""defination of square based on 3-square.py"""


class Square:
    """defination of square by it's size"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('size should be int')

        if size < 0:
            raise ValueError('size should be >= 0')
        self.__size = size

    def area(self):
        area = self.__size * self.__size
        return area
