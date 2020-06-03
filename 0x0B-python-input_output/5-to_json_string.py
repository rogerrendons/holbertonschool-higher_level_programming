#!/usr/bin/python3
"""
    Write a function that returns the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """ Returns JSON Rep Object """
    return (json.dumps(my_obj, sort_keys=True))
