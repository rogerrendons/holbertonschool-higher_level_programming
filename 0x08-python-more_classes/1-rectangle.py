#!/usr/bin/python3
""" empty class Rectangle that defines a rectangle """


class Rectangle:
    """ class Rectangle """

    def __init__(self, width=0, height=0):
        """ initializes sizes """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter width """
        return self.__width

    @property
    def height(self):
        """ getter height """
        return self.__height

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
