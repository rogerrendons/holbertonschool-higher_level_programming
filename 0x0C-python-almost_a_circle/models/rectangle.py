#!/usr/bin/python3
""" Write the class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ Class rectangle inherits from class base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ method for Rectangle calss """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """ getters """
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    """ setters """
    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError('width must be an integer')
        if val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError('height must be an integer')
        if val <= 0:
            raise ValueError('height must be > 0')
        self.__height = val

    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError('x must be an integer')
        if val < 0:
            raise ValueError('x must be >= 0')
        self.__x = val

    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError('y must be an integer')
        if val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val

    def area(self):
        """ method for area formula """
        return self.width * self.height

    def display(self):
        """ method print rectangle figure"""

        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(' ', end='')
            for _ in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """ Representation of rectangle figure return """
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}\
            ".format(self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ Object update specified values """
        leng = len(args)
        if ((args and leng < 6) and (args[0] != None) and (args[0] != "")):
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Dictionary of rectangle """
        return {"x": self.__x, "y": self.__y, "id": self.id, "height": self.__height, "width": self.__width,}

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string write to a file """
        with open(cls.__name__ + '.json', mode='w', encoding='utf-8') as file:
            listres = []
            if (list_objs):
                for rec in list_objs:
                    listres.append(rec.to_dictionary())
                listres = cls.to_json_string(listres)
                file.write(listres)
            else:
                file.write('[]')
