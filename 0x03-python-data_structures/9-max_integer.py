#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    for rec in range(len(my_list)):
        if max < my_list[rec]:
            max = my_list[rec]
    return (max)
