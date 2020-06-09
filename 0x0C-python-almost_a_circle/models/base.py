#!/usr/bin/python3
import json


class Base:
    """ Define module class Base """

    __nb_objects = 0    # Private class atributte#

    def __init__(self, id=None):
        """ Base instance, constructor class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return dict representation JSON """
        if list_dictionaries is None or list_dictionaries == []:
            return("[]")
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ String to list of string """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """ return atributes in dictionary """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == "Rectangle":
            figure = Rectangle(16, 7)
        elif cls.__name__ == "Square":
            figure = Square(7)
        figure.update(**dictionary)
        return figure

    @classmethod
    def load_from_file(cls):
        """ load from a file an object """
        load = []
        try:
            with open(cls.__name__ + '.json', mode='r', encoding='utf-8') as\
                 file:
                listres = json.dumps(json.load(file))
        except FileNotFoundError:
            return load
        list_dictionaries = cls.from_json_string(listres)
        for rec in list_dictionaries:
            load.append(cls.create(**rec))
        return load
