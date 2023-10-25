#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class to represent a square and perform operations on it.

    Attributes:
        None
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): Length of the square's side.
            x (int): X-coordinate of the top-left corner.
            y (int): Y-coordinate of the top-left corner.
            id (int): Object identifier (optional).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the length of the square's side
        (equivalent to the width of the rectangle)."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the length of the square's side
        (equivalent to the width and height of the rectangle).

        Args:
            value (int): New length of the side.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square]\
        ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Assigns arguments to attributes,
        supports both arguments and key-value pairs.

        Args:
            *args: Arguments to update the attributes
            (in the order: id, size, x, y).
            **kwargs: Key-value pairs to update the attributes.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
            self.width = self.size
            self.height = self.size
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
                if key == "size":
                    self.width = value
                    self.height = value

    def to_dictionary(self):
        """
        Returns a dictionary representing the Square object.

        Returns:
            dict: Dictionary with the object's attributes.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
