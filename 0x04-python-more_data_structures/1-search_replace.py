#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return [replace if num == search else num for num in my_list]
