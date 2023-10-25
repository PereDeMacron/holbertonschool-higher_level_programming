#!/usr/bin/python3
"""Define a function that returns the dictionary description with a simple data structure for JSON."""

def class_to_json(obj):
    """Returns the dictionary with a simple data structure."""
    return obj.__dict__
