#!/usr/bin/python3
for a in range(10):
    for b in range(a+1,10):
        if a == 8 and b == 9:
            print("{:d}{:d}".format(a, b))
            continue
        print("{:d}{:d}".format(a, b), end=", ")
