#!/usr/bin/python3
"""define class for rectangle"""


class Rectangle:
    """represent rectangle."""

    def __init__(self, width=0, height=0):
        """Initialization of new Rectangle.

        Args:
            width (int): width of new rectangle.
            height (int): height of new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
