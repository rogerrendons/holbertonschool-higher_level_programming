#!/usr/bin/python3
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
