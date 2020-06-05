#!/usr/bin/python3
"""
0-add_integer.py file
Functions:
-> add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """"
    Function that returns a + b

     Args:
        a (int, float): The first parameter
        b (int, float): The second parameter

    Returns:
        The result of the operation

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
