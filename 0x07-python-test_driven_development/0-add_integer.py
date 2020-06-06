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
    if (a is None or (not isinstance(a, int) and not isinstance(a,float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
