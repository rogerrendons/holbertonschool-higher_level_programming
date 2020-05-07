#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if type(roman_string) == str:
        largest = 1
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for read in roman_string[::-1]:
#           if read in roman:
            if roman[read] >= largest:
                result = result + roman[read]
                largest = roman[read]
            else:
                result = result - roman[read]
    return result
