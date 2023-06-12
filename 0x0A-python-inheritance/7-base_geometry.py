#!/usr/bin/python3
"""
Define base geometry class.
"""


class BaseGeometry:
    """Represent base"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate parameter as int.
        Args:
            name (str): name of parameter.
            value (int): parameter to validate.
        Raises:
            TypeError: If value is not int.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
