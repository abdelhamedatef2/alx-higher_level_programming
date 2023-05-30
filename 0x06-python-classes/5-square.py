#!/usr/bin/python3
"""define square based on 4-square.py"""


class Square:
    """implementation of square"""
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
        area = self.__size ** 2
        return area

    def my_print(self):
        if self.__size != 0:
            for i in range(self.__size):
                print('#' * self.__size)
        else:
            print("")
