#!/usr/bin/python3
"""def a function that returns the dictionary
description with simple data structure for JSON """
def class_to_json(obj):
    """Returns the dictionary with simple data struct"""
    return obj.__dict__
