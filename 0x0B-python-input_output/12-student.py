#!/usr/bin/python3
"""
    Write a class Student that defines a student by: (based on 11-student.py)
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, atr=None):
        if atr is not None:
            dic = {}
            for i in atr:
                if i in self.__dict__:
                    dic[i] = self.__dict__[i]
            return dic
        return self.__dict__
