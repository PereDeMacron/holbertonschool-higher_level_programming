#!/usr/bin/python3
"""def a JSON writing on file function."""
import json


def save_to_json_file(my_obj, filename):
    """object to a text file using JSON file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
