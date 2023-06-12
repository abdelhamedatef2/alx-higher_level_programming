#!/usr/bin/python3
"""Define base class for geometry"""


class BaseGeometry:
    """represent base"""

    def area(self):
        """raise exception indicate that area() is not implemented"""
        raise Exception("area() is not implemented")
