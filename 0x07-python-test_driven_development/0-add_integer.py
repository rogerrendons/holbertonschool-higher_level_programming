#!/usr/bin/python3
"""
    Add 2 integers
    imput a 2 numbers for a sum.

"""


def add_integer(a, b=98):
    """
        Function add 2 integers
    """
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    Res = int(a) + int(b)
    return (Res)
