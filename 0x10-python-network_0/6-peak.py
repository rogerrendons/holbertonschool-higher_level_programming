#!/usr/bin/python3
""" Find unsorted integers peak """

def find_peak(list_of_integers):
    if list_of_integers:
        for First, Last in enumerate(list_of_integers):
            if First > 1:
                if Last < list_of_integers[First-1]:
                    if list_of_integers[First-2] < list_of_integers[First-1]:
                            return list_of_integers[First-1]
        return max(list_of_integers)
    else:
        return
