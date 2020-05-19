#!/usr/bin/python3
""" class Square """


class Square:
    """ define size Square """
    def __init__(self, size=0):
        """ size Square to size for instance and probe if a integer"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    """ resolve area of Square """
    def area(self):
        return (self.__size ** 2)
