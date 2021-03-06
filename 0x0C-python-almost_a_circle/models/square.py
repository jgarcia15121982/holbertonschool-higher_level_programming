#!/usr/bin/python3
"""class Square"""

from models.rectangle import *


class Square(Rectangle):
    """class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize Square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get value of size"""
        return self.height

    @size.setter
    def size(self, size):
        """set value of size"""
        self.width = size
        self.height = size

    def __str__(self):
        """method __str__ that returns
           the square description
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.height)

    def update(self, *args, **kwargs):
        """method that update
            values of the class
        """
        if args and len(args) > 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            if kwargs.get('id'):
                self.id = kwargs['id']
            if kwargs.get('size'):
                self.size = kwargs['size']
            if kwargs.get('x'):
                self.x = kwargs['x']
            if kwargs.get('y'):
                self.y = kwargs['y']

    def to_dictionary(self):
        """Public method that returns the dictionary
            representation of a Square
        """
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['size'] = self.height
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        return my_dict
