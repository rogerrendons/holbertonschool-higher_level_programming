#!/usr/bin/python3
""" class Square """


class Square:
    """ define size Square """
    def __init__(self, size=0):
        """ size Square to size for instance and probe if a integer"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """ resolve area of Square """
    def area(self):
        return (self.__size ** 2)

    """ is a getter size """
    @property
    def size(self):
        return self.__size

    """ setter size and probe if a integer"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ print Square iqual to size"""
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for vert in range(self.__size):
                for horiz in range(self.__size):
                    print('#', end="")
                print("")
