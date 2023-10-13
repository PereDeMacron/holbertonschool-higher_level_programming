#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self._height = value

    def area(self):
        if self.width or self.height == 0:
            return 0
        else:
            return (self._width * self._height)
    
    def perimeter(self):
        return ((self.width * 2) + (self.height * 2))
    

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ("")

        rectangle = []
        for i in range(self._height):
            [rectangle.append('#') for j in range(self._width)]
            if i != self._height - 1:
                rectangle.append("\n")
        return (''.join(rectangle))

    def __repr__(self):
        rect = "Rectangle(" + str(self._width)
        rect += ", " + str(self._height) + ")"
        return (rect)

    def __del__(self):
        print("Bye rectangle...")
