#!/usr/bin/python3
"""Define Rectangle class"""


class Rectangle:
    """define rectangle."""

    def __init__(self, width=0, height=0):
        """Initialization of new Rectangle

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of Rectangle."""
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
        """Get/set height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of Rectangle.

        Returns:
            int: area of rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter of Rectangle.

        Returns:
            int: perimeter of rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
