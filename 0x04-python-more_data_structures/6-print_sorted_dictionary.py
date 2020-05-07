#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        for ord in sorted(a_dictionary):
	        print("{:s}: {}".format(ord, a_dictionary[ord]))
