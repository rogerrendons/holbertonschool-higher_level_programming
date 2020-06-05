#!/usr/bin/python3
"""
    Write a function that returns an object
    (Python data structure) represented by a JSON string
"""


def from_json_string(my_str):
    """ Return Object """

    from json import loads
    return json.loads(my_str)
