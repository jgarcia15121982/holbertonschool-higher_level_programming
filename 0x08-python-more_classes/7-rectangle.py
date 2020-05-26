#!/usr/bin/python3
"""Area and Perimeter"""


class Rectangle():
    """class that represents a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes instance of Rectangle. If either width or height
        are ommitted, they are set to 0 by default
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    def __str__(self):
        """Prints a rectangle with the character #
        """
        return_val = ""
        width = self.width
        height = self.height
        if width != 0 and height != 0:
            for i in range(height):
                return_val += str(self.print_symbol) * width
                if i != height - 1:
                    return_val += "\n"
        return return_val

    def __repr__(self):
        """Returns a string representation of the
        rectangle to be able to recreate a new
        instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete an object
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Returns a width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets width to positive integer value"""
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
        """Sets height to positive integer value"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
