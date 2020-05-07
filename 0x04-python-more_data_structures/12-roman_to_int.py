#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if type(roman_string) == str:
        largest = 1
        r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for read in roman_string[::-1]:
            if r[read] >= largest:
                result = result + r[read]
                largest = r[read]
            else:
                result = result - r[read]
    return result
