#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle():
    """class that represents a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns a width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter method"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Returns a height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Height setter method"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
