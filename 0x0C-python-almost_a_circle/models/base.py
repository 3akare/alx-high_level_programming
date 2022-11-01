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

    @staticmethod
    def from_json_string(json_string):
        """
            Return the list of JSON string
            representation
        """
        if (json_string is None or json_string == []):
            return ([])
        return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        '''loads an instance'''

        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return (new)

    @classmethod
    def load_from_file(cls):
        ''' returns a list of instances '''
        from os import path
        filename = cls.__name__ + '.json'
        if not path.isfile(filename):
            return []
        with open(filename, 'r') as f:
            return [cls.create(**arg) for arg in
                    cls.from_json_string(f.read())]

    @classmethod
    def create(cls, **dictionary):
        '''loads an instance'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''makes object in csv file'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                             for obj in list_objs]
            else:
                list_objs = [[obj.id, obj.size, obj.x, obj.y]
                             for obj in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding="utf-8") as content:
            writer = csv.writer(content)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''retrieve an object from the csv file'''
        from models.rectangle import Rectangle
        from models.square import Square
        load = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as content:
            reader = csv.reader(content)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    string = {"id": row[0], "width": row[1], "height": row[2],
                              "x": row[3], "y": row[4]}
                else:
                    string = {"id": row[0], "size": row[1],
                              "x": row[2], "y": row[3]}
                load.append(cls.create(**string))
        return load
