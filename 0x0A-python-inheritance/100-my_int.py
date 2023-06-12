#!/usr/bin/python3
"""Define class MyInt inherit from int."""


class MyInt(int):
    """Custom int class that inverts == , != operators"""

    def __eq__(self, value):
        """Override == operator ccheck inequality"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator checks equality."""
        return self.real == value
