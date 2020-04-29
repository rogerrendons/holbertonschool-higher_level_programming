#!/usr/bin/python3
def uppercase(str):
    for char in str:
        let = 0
        if ord(char) > 96 and ord(char) < 123:
            let = -32
        print("{:s}".format(chr(ord(char) + let)), end='')
    else:
        print()
