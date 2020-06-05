#!/usr/bin/python3
"""
    Create a function def pascal_triangle(n): that returns a list
    of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """ The Pascal triangle """

    list0 = []
    if n <= 0:
        return (list0)

    acum = []
    filerow = []

    for num in range(n):
        filerow = [1]
        if num > 0:
            for rec in range(num):
                filerow.append(sum(acum[-1][rec:rec + 2]))
        acum.append(filerow)
    return acum
