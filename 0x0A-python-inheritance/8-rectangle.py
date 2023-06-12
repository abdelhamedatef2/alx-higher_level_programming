#!/usr/bin/python3
"""That define class Rectangle that inherits BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """That represents rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialization of new Rectangle.
        Args:
            width (int): width of new Rectangle.
            height (int): height of new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
