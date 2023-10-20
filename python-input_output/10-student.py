#!/usr/bin/python3
"""script convert a Student object to a dictionary"""
class Student:
    """class represents a student with attributes"""

    def __init__(self, first_name, last_name, age):
        """Constructor for the Student class
        
        Parameters:
        - first_name (str): The first name of the student
        - last_name (str): The last name of the student
        - age (int): The age of the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert the Student object to a dictionary

        Returns:
        a dictionary containing object attribute"""
        class_d = self.__dict__
        sel_d = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return class_d

                if attr in class_d:
                    sel_d[attr] = class_d[attr]
            return sel_d

        return class_d
