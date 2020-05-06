#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resul = []
    for reco in my_list:
        if reco % 2 is 0:
            resul.append(True)
        else:
            resul.append(False)
    return resul
