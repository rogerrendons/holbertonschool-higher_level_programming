#!/usr/bin/python3
""" class Square """


class Square:
    """ define size Square """
    def __init__(self, size=0, position=(0, 0)):
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


    @size.setter
    def size(self, value):
        """ setter size and probe if a integer """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ print Square iqual to size """
        if self.__size != 0:
            for a in range(self.__position[1]):
                print()
            for a in range(self.size):
                for b in range(self.__position[0]):
                    print(' ', end='')
                for c in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()

    @property
    def position(self):
        """ property position definition """
        return self.__position

    @position.setter
    def position(self, value):
        """ Position """
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
