#!/usr/bin/python3


def add_integer(a, b=98):
    """"
    Function that returns a + b

     Args:
        a (int, float): The first parameter
        b (int, float): The second parameter

    Returns:
        The result of the operation

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
