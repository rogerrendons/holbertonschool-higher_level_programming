#!/usr/bin/python3
""" Find peak in unsorted integers """

def find_peak(list_of_integers):
    ''' Find Peak Class. '''

    lst = []
    lst = list_of_integers
    if list_of_integers:
        if len(list_of_integers) % 3 == 0:
            lst.pop(0)
            return max(lst)
        else:
            return max(lst)
    return None
