#!/usr/bin/python3
""" class Square """


class Square:
    """ define size Square """
    def __init__(self, size=0, position=(0, 0)):
        """ size Square to size for instance and probe if a integer"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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

    """ print Square iqual to size """
    def my_print(self):
        if self.__size != 0:
            for a in range(self.__position[1]):
                print("")
            for a in range(self.size):
                for b in range(self.__position[0]):
                    print(' ', end='')
                for c in range(self.__size):
                    print('#', end='')
                print("")
        else:
            print("")

    """ property position definition """
    @property
    """ position definition """
    def position(self):
        return self.__position

    """ Position """
    @position.setter
    def position(self, value):
        if type(value) is tuple:
            if len(value) != 2:
                raise TypeError
                ("position must be a tuple of 2 positive integers")
            else:
                for x in range(len(value)):
                    if value[x] < 0:
                        raise TypeError
                        ("position must be a tuple of 2 positive integers")
            self.position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
