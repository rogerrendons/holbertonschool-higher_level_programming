#!/usr/bin/python3
""" initial base.py """
import json


class Base:
    """ Define module class Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Base instance, constructor class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """ return atributes in dictionary """
        # from models.rectangle import Rectangle
        # from models.square import Square
        if cls.__name__ == "Rectangle":
            figure = cls(16, 7)
        elif cls.__name__ == "Square":
            figure = cls(7)
        return (figure.update(**dictionary))

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

