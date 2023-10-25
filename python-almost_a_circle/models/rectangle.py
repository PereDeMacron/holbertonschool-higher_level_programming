#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """
    Class to represent a rectangle and perform operations on it.

    Attributes:
        current_id (int): Class-level attribute to track the current ID.
    """

    current_id = 0

    @classmethod
    def increment_id(cls):
        """
        Increments the current ID and returns the new value.

        Returns:
            int: New value of the current ID.
        """
        cls.current_id += 1
        return cls.current_id

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the top-left corner.
            y (int): Y-coordinate of the top-left corner.
            id (int): Object identifier (optional).

        Note:
            If ID is not specified, it is automatically incremented.
        """
        super().__init__(id)
        if id is None:
            self.id = self.__class__.increment_id()
        else:
            self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): New width.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): New height.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns the X-coordinate of the top-left corner
        of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the X-coordinate of the top-left corner of the rectangle.

        Args:
            value (int): New X-coordinate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than zero.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns the Y-coordinate of the top-left corner of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the Y-coordinate of the top-left corner of the rectangle.

        Args:
            value (int): New Y-coordinate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than zero.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """
        Displays the rectangle using '#' characters with offsets in x and y.

        Note:
            It first prints empty lines for the y-offset and then prints '#'
            characters for the rectangle.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Assigns arguments to attributes, supports both arguments and
        key-value pairs.

        Args:
            *args: Arguments to update the attributes
            (in the order: id, width, height, x, y).
            **kwargs: Key-value pairs to update the attributes.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Returns a dictionary representing the Rectangle object.

        Returns:
            dict: Dictionary with the object's attributes.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
