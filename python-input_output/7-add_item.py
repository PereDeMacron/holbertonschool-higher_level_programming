#!/usr/bin/python3
"""A module for saving Python objects to a JSON file."""

import json

def save_to_json_file(my_obj, filename):
    """
    Save a Python object to a JSON file.

    This function takes a Python object and a filename as arguments and writes
    the object's JSON representation to the specified file.

    Args:
        my_obj: The Python object to be saved to a JSON file.
        filename (str): The name of the file where the JSON representation
            will be stored.

    Raises:
        IOError: If there is an issue with opening or writing to the file.

    Example:
        # Save a Python dictionary to a JSON file
        data = {'name': 'John', 'age': 30, 'city': 'New York'}
        save_to_json_file(data, 'data.json')
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
