#!/usr/bin/python3
"""
    Write a function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """ Create object with json file"""
    with open(filename) as file:
        return json.load(file)
