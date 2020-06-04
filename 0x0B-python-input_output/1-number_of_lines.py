#!/usr/bin/python3
"""Number of lines module"""


def number_of_lines(filename=""):
    """Function that returns the number
    of lines of a text"""
    nb_line = 0
    with open(filename, mode='r', encoding="utf=8") as myFile:
        for numline in myFile:
            nb_line += 1
    return nb_line
    myFile.close()
