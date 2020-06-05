#!/usr/bin/python3
"""
    Write a function that returns an object
    (Python data structure) represented by a JSON string
"""


def from_json_string(my_str):
    """ Return Object """

    import json
    return json.loads(my_str)
