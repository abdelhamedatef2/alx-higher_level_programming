#!/usr/bin/python3
"""defines str-to-JSON function."""
import json


def to_json_string(my_obj):
    """returns JSON representation of str object."""
    return json.dumps(my_obj)
