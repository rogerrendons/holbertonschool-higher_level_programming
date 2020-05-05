#!/usr/bin/python3
def max_integer(my_list=[]):
    MV = 0
    if (len(my_list) == 0):
        return ("None")    
    for rec in range(len(my_list)):
        if MV < my_list[rec]:
            MV = my_list[rec]
    return (MV)
