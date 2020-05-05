#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    MV = my_list[0]
    for recor in my_list:
        if recor > MV:
            MV = recor
    return MV
