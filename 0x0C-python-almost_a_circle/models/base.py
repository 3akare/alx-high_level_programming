#!/usr/bin/python3
"""Defines a base model class"""

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
