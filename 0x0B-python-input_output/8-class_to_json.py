#!/usr/bin/python3
"""defination of Python class-to-JSON function."""


def class_to_json(obj):
    """returns dictionary represntation of simple data struct"""
    return obj.__dict__
