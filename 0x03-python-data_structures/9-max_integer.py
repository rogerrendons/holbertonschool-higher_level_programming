#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if (len(my_list) == 0):
        return ("None")    
    for rec in range(len(my_list)):
        if max < my_list[rec]:
            max = my_list[rec]
    return (max)
