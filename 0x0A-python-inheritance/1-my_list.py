#!/usr/bin/python3
"""Class that inheritance from MyList"""


class MyList(list):
    """class that inheritance from a list"""

    def print_sorted(self):
        """print an ascending sorted list"""
        print(sorted(self))
