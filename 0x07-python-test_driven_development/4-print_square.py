#!/usr/bin/python3
"""
4-print_square.py file
Functions:
-> print_square(size)

"""


def print_square(size):
    """
    Function that prints a square with the character #.

    Args:
        a (int, float): The size of the square

    Returns:
        Nothing. The function prints the square

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
