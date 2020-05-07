#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new = a_dictionary.copy()
        for rec in new:
            new[rec] = new[rec] * 2
    return (new)
