#!/usr/bin/python3
"""def a class BaseGeometry"""
class BaseGeometry:
    """BaseGeometry"""

    def area(self):
        """don't implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate integer(value)
        Args:
            name(str) parameter name
            value(int) parameter to be validate
        Raises:
            TypeError: if the value is not an int
            ValueError:if the value is small to 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
