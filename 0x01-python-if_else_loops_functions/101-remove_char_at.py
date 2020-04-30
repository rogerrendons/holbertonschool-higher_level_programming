#!/usr/bin/python3
def remove_char_at(str, n):
    Result = ""
    for Iter in range(len(str)):
        if (Iter != n):
            Result += str[Iter]
    return (Result)
