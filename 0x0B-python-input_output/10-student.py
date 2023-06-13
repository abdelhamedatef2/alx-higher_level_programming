#!/usr/bin/python3
"""defination of class Student."""


class Student:
    """represen student."""

    def __init__(self, first_name, last_name, age):
        """initialization of new Student.
        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get dictionary representation of Student.
        If attributess is list of strs, it represents only the attributes
        included in list.
        Args:
            attrs (list): (Optional) attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
