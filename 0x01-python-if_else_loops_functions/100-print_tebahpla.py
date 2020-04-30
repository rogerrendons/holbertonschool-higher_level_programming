#!/usr/bin/python3
min = True
for cont in range(122, 96, -1):
    if not min:
        cont -= 32
    print("{}".format(chr(cont)), end='')
cont = not cont
