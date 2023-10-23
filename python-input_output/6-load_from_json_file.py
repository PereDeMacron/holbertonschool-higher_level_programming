#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        data: The Python object created from the JSON data in the file.

    This function reads the content of a JSON file and deserializes it into a Python object.
    It is commonly used to load configuration data, data exchange, or any other JSON-based data
    into a Python script.

    Example:
    If you have a JSON file named 'data.json' with the following content:
    {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    You can use this function to load the JSON data from the file like this:
    >>> loaded_data = load_from_json_file("data.json")
    >>> print(loaded_data)
    {'name': 'John', 'age': 30, 'city': 'New York'}

    Note that the 'filename' argument should be a valid path to the JSON file.
    """

    with open(filename, 'r') as file:
        data = json.load(file)
    
    return data
