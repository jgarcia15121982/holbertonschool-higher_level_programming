#!/usr/bin/python3
"""class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
          of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
           of list_objs to a file
        """
        if list_objs is None:
            nw_list = []
        else:
            nw_list = []
            for obj in list_objs:
                nw_list.append(obj.to_dictionary())
        file_nm = cls.__name__ + '.json'
        with open(file_nm, mode="w+", encoding='utf-8') as myFile:
            json_str = Base.to_json_string(nw_list)
            myFile.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            json_string = "[]"
        return json.loads(json_string)
