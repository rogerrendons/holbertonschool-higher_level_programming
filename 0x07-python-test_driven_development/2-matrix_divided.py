#!/usr/bin/python3
"""

    Function that divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """

        Divide all numbers in a matrix
        Args:
            matrix: Matrix Numbers
            div:

        Return: the result division

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    l = []
    AuxList = []
    RLen = len(matrix[0])
    for Rec in matrix:
        if len(Rec) != RLen:
            raise TypeError("Each row of the matrix must have the same size")

    Aux = []
    Acum = 0
    for x in matrix:
        if not isinstance(x, list):
            raise TypeError("matrix must be a matrix (list of lists)\
                            of integers/floats")
        Aux.append([])
        for y in x:
            if not isinstance(y, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

            Aux[Acum].append(round(y / div, 2))
        Acum += 1
    return Aux
