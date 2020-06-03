#!/usr/bin/python3
"""Function that returns True if the object
   is an instance of a class that inherited from
   (directly or indirectly) from the specified
   class; otherwise False."""


def inherits_from(obj, a_class):
    """Function that returns True if the object
    is an instance of a class that inherited from
    (directly or indirectly) from the specified
    class; otherwise False."""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
