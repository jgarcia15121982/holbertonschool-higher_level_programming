#!/usr/bin/python3
"""class Base"""


class Base():
    """base class for the Almost a Circle project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
