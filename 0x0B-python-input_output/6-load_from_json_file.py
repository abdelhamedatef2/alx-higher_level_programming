#!/usr/bin/python3
"""defination of JSON file-reading function."""
import json


def load_from_json_file(filename):
    """create Python obj from JSON file."""
    with open(filename) as f:
        return json.load(f)
