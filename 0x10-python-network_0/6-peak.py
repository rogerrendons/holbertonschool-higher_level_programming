#!/usr/bin/python3
""" Find peak in unsorted integers """

def find_peak(list_of_integers):
    ''' Find Peak Class. '''

    
    if list_of_integers:
        if len(list_of_integers) % 3 == 0:
            list_of_integers.pop(0)
            return max(list_of_integers)
        else:
            return max(list_of_integers)
    return None
