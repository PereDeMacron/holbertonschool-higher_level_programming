#!/usr/bin/python3
"""defines a class and a class checker function."""
def is_kind_of_class(obj, a_class):
    """check if obj is an instance
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns: if obj is an instance returns true
        else returns false"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
