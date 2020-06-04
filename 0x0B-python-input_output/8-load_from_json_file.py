#!/usr/bin/python3
"""Create object from a JSON file module"""


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    import json
    with open(filename, mode="r", encoding='utf-8') as myFile:
        return json.load(myFile)
