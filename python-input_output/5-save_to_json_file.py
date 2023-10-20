#!/usr/bin/python3
import json
"""def a fonction that write an Object to a text file,
using a JSON representation"""
def save_to_json_file(my_obj, filename):
    """Save the given object to a text file using JSON representation.

    Args:
        my_obj: object to be serialized and save
        filename (str): the name of the file to save the JSON data in"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
