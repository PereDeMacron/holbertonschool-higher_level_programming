#!/usr/bin/python3
"""define a  focntion for check class"""
def is_same_class(obj, a_class):
    """if the object is exactly an instance of the specified class
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is different as an instance of a_class - False.
        else return True"""
    if type(obj) != a_class:
        return False
    else:
        return True
