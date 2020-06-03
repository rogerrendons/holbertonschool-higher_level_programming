#!/usr/bin/python3
"""
    Write a function that writes an Object to a text file,
    using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ JSON file saved"""
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj, sort_keys=True, ensure_ascii=False))
