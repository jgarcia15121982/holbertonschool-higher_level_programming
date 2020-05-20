#!/usr/bin/python3
"""Class Square"""


class Square:
    """class that represents a Square"""

    def __init__(self, size=0):
        """Initializes the class"""
        self.size = size

    @property
    def size(self):
        """Returns a size"""
        return self.__size

    @size.setter
    def size(self, size):
        """error handling"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the area of a square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print()
