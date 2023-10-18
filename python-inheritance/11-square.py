#!/usr/bin/python3
"""def a class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ Represent a square from rectangle class """
    def __init__(self, size):
        """ init new Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ returns a str with the area """
        return super().area()

    def __str__(self):
        """ returns a printable string """
        return "[Square] {}/{}".format(self.__size, self.__size)
