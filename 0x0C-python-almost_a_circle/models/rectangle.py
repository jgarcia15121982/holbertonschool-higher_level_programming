#!/usr/bin/python3
"""class Rectangle"""

from models.base import *


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get value of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set value of width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """get value of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set value of height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """get value of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set value of x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """get value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set value of y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """method area"""
        return self.__width * self.__height

    def display(self):
        """method display"""
        s = " " * self.__x
        tag = "#" * self.__width
        line = s + tag
        for h in range(self.__y):
            print("")
        for i in range(self.__height):
            print(line)

    def __str__(self):
        """method __str__ that returns
           the rectangle description
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """method that update
            values of the class
        """
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            if len(args) == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
        else:
            if kwargs.get('id'):
                self.id = kwargs['id']
            if kwargs.get('width'):
                self.__width = kwargs['width']
            if kwargs.get('height'):
                self.__height = kwargs['height']
            if kwargs.get('x'):
                self.__x = kwargs['x']
            if kwargs.get('y'):
                self.__y = kwargs['y']

    def to_dictionary(self):
        """Public method that returns the dictionary
            representation of a Rectangle
        """
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['width'] = self.width
        my_dict['height'] = self.height
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        return my_dict
