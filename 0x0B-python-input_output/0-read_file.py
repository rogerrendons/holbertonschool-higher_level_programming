#!/usr/bin/python3
""" Function read_file """


def read_file(filename=""):
    """ Functionthat reads a text file and prints to stdout """
    with open(filename, mode="r", encoding='utf-8') as myfile:
        print(myfile.read(), end="")
