#!/usr/bin/python3
"""Class Square"""


class Square:
    """class that represents a Square"""

    def __init__(self, size=0):
        """Initializes with error handling"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Defines the area of a square"""
        return self.__size * self.__size
