#!/usr/bin/python3
"""Save object to a file module"""


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation"""
    import json
    with open(filename, "w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
