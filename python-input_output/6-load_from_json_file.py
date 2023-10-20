#!/usr/bin/python3
import json
"""def a fonctiont that creates an Object from a “JSON file”"""
def load_from_json_file(filename):
    """
    create object from JSON file

    Args:
        filename (str): The name of the JSON file

    Returns:
        data: the python object created from the JSON uin the file
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    
    return data
