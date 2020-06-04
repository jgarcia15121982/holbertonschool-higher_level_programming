#!/usr/bin/python3
"""Read n lines module"""


def read_lines(filename="", nb_lines=0):
    """Function that reads n lines of a text file"""
    number_of_lines = __import__('1-number_of_lines').number_of_lines
    count = 0
    num_file_lines = number_of_lines(filename)
    with open(filename, mode='r', encoding="utf=8") as myFile:
        if nb_lines <= 0 or nb_lines >= num_file_lines:
            print(myFile.read(), end='')
        else:
            while count != nb_lines:
                print(myFile.readline(), end='')
                count += 1
