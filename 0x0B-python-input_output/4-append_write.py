#!/usr/bin/python3
"""Module Append to a file"""


def append_write(filename="", text=""):
    """Function that appends a string to a end of a
       text file (UTF8) and returns the number of
       characters added"""
    with open(filename, mode='a+', encoding="utf=8") as myFile:
        return(myFile.write(text))
