#!/usr/bin/python3
""" Representation of rectangle figure return """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square instance inherit class definition"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Method for class square """
        super().__init__(size, size, x, y, id)

    """ getter """
    @property
    def size(self):
        return self.width

    """ setter """
    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def __str__(self):
        """ Representation of square figure return """
        return ("[Square] ({}) {:d}/{:d} - {:d}".format(
            self.id, self.__x, self.__y, self.___width))

    def update(self, *args, **kwargs):
        """ Object update specified values """
        leng = len(args)
        if ((args and leng < 5) and (args[0] is not None) and (args[0] != "")):
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                return
            return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Dictionary of square """
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
