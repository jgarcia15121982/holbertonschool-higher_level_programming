#!/usr/bin/python3
""" class Rectangle"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle. Inherits from class
       BaseGeometry"""

    def __init__(self, width, height):
        """init class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Function that print rectangle information"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """Returns rectangle area"""
        return self.__width * self.__height
