#!/usr/bin/python3
"""
    Write a function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ Append string end of file """
    with open(filename, mode='a', encoding='utf-8') as file:
        return (file.write(text))
