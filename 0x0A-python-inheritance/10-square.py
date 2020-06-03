#!/usr/bin/python3
"""Square class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class Square, inherits from class Rectangle"""
    def __init__(self, size):
        """Initialize private instance attribute size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
