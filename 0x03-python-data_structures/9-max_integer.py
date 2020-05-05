#!/usr/bin/python3
def max_integer(my_list=[]):
    MV = my_list[0]
    if (len(my_list) == 0):
        return ("None")
    for rec in my_list:
        if rec > MV:
            MV = rec
    return (MV)
