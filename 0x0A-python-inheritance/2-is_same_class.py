#!/usr/bin/python3
"""Function that returns the object is exactly
   an instance of the specified class"""


def is_same_class(obj, a_class):
    """Function that returns True
        if the object is exactly an
        instance of the specified class
        otherwise False."""
    if type(obj) is a_class:
        return True
    else:
        return False
