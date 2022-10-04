#!/usr/bin/python3
"""Defines a base model class"""
import json


class Base:
    """
    Represent the base model for all other classes in project 0x0C*
    Attibutes:
        __nb_objects (int): The nunmber of instantiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize a new Base

            Args:
                id(int): the indentity of a new Base
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Return the JSON serializartion of a list of dicts.

            Args:
                list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ('[]')
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Writes the JSON string represntation to a file

            Args:
                list_objs (list): A list of instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write('[]')
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))
