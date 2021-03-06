#!/usr/bin/python3
""" Write a function that returns the number of lines of a text file """


def number_of_lines(filename=""):
    """ Counter lines """
    Counter = 0
    with open(filename, mode="r", encoding='utf-8') as file:
        for _ in file:
            Counter += 1
    return Counter
