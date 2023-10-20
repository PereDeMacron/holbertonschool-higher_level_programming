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

    def to_json(self):
        """Convert the Student object to a dictionary

        Returns:
        a dictionary containing object attribute"""
        return self.__dict__

