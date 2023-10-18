#!/usr/bin/python3
"""define a class checking fonction"""
def inherits_from(obj, a_class):
    """check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        if obj is an inheritance of a_class return true
        else return false"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
