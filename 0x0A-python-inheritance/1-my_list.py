#!/usr/bin/python3
"""
    Write a class MyList that inherits from list
"""


class MyList(list):
    """
        inherts from list class
    """

    def print_sorted(self):
        """
            method print list
        """
        print(list(sorted(self)))
