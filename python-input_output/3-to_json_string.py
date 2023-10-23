#!/usr/bin/python3
import json

def to_json_string(my_obj):
    """
    This function takes an object as input and returns its JSON representation.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: A JSON string representation of the input object.
    """
    return json.dumps(my_obj)
