#!/usr/bin/python3
"""class Square"""

from models.rectangle import *


class Square(Rectangle):
    """class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize Square class"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get value of size"""
        return self.__size

    @size.setter
    def size(self, size):
        """set value of size"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size

    def __str__(self):
        """method __str__ that returns
           the square description
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
