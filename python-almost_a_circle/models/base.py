#!/usr/bin/python3
"""Task 1"""


import json
import os


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        That method returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
         That method that writes the JSON string representation of \
            list_objs to a file
        """
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as x:
            if list_objs is None:
                x.write("[]")
            else:
                obj = []
                for i in list_objs:
                    obj.append(i.to_dictionary())
                x.write(cls.to_json_string(obj))

    @staticmethod
    def from_json_string(json_string):
        """
        That method returns the list of the JSON string representation \
            json_string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new object
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file
        """
        if os.path.exists(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as x:
                data = x.read()
                if data:
                    list = cls.from_json_string(data)
                    return [cls.create(**jstring)
                            for jstring in list]
                else:
                    return []
        else:
            return []
