#!/usr/bin/python3
""" Write a function that reads n lines of
    a text file (UTF8) and prints it to stdout
"""


def read_lines(filename="", nb_lines=0):
    """ Read lines """
    Counter = 0
    with open(filename, mode="r", encoding='utf-8') as file:
        if nb_lines <= 0:
            print(file.read(), end='')
        else:
            for line in file:
                if (Counter < nb_lines):
                    print(line, end="")
                    Counter += 1
