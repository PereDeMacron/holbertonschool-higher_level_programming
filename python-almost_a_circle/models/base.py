#!/usr/bin/python3

import json
import os


class Base:
    """Base class for managing objects and saving them in JSON format.

    Attributes:
        __nb_objects (int): A class-level attribute to keep
        track of the number of objects created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new object.

        Args:
            id (int): The object's identifier. If not specified,
            a unique identifier is assigned.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries into a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries to convert.

        Returns:
            str: JSON string representing the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            cls (class): The class to which the objects belong.
            list_objs (list): List of objects to save.
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = f"{class_name}.json"
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)

        with open(filename, "w") as file:
            file.write(json_string)

    @classmethod
    def from_json_string(cls, json_string):
        """
        Converts a JSON string into a list of dictionaries.

        Args:
            cls (class): The class to which the objects belong.
            json_string (str): JSON string to convert.

        Returns:
            list: List of dictionaries.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new object from a dictionary of initial values.

        Args:
            cls (class): The class from which to create the object.
            **dictionary (dict): Dictionary of initial values.

        Returns:
            object: New object created with the specified values.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(0)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads objects from a JSON file and creates
        instances using the `create` method.

        Args:
            cls (class): The class from which to create the objects.

        Returns:
            list: List of objects created.
        """
        filename = f"{cls.__name__}.json"

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins

    def to_dictionary(self):
        """
        Converts the object into a dictionary representing its attributes.

        Returns:
            dict: Dictionary of the object's attributes.
        """
        return self.__dict__

    def update(self, *args, **kwargs):
        """
        Updates the object's attributes based on the
        specified arguments or key-value pairs.

        Args:
            *args: Arguments to update the attributes
            (in the order: id, width, height, x, y).
            **kwargs: Key-value pairs to update the attributes.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                if i < len(attrs):
                    setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
