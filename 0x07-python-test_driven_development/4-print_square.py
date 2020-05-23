#!/usr/bin/python3
""" class Square """


def print_square(size):
    """

        Function to print square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for vert in range(size):
            for horiz in range(size):
                print('#', end="")
            print("")
