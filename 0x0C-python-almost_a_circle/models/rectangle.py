#!/usr/bin/python3
"""class Rectangle"""

from models.base import *


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns a width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter method"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
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
        if height <= 0:
            raise ValueError("heigth must be > 0")
        self.__height = height

    @property
    def x(self):
        """Returns x"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter method"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Returns y"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter method"""
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
