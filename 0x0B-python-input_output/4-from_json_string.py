#!/usr/bin/python3
"""defenation of JSON-to-object function."""
import json


def from_json_string(my_str):
    """return Python object representation of JSON str"""
    return json.loads(my_str)
