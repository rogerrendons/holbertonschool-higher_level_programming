#!/usr/bin/python3
""" Find peak in unsorted integers """


def find_peak(list_of_integers):
    """function find integers"""

    if len(list_of_integers) == 0:
        return None
    lists, lng = list_of_integers, len(list_of_integers)
    midt = lng // 2
    if (midt == lng - 1 or lists[midt] >= lists[midt + 1]):
        if (midt == 0 or lists[midt] >= lists[midt - 1]):
            return lists[midt]
    if midt != lng - 1 and lists[midt + 1] > lists[midt]:
        return find_peak(lists[midt + 1:])
    return find_peak(lists[:midt])
