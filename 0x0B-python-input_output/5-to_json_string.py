#!/usr/bin/python3
"""JSON print Module"""


def to_json_string(my_obj):
    """function that returns the JSON
       representation of an object (string)"""
    import json
    return json.dumps(my_obj)
