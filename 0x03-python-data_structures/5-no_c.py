#!/usr/bin/python3
def no_c(my_string):
    result = []
    for char in my_string:
        if char != 'C' and char != 'c':
            result.append(char)
    return (''.join(result))
