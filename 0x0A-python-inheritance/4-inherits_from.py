#!/usr/bin/python3
"""
    Module inherits_from
"""


def inherits_from(obj, a_class):
    """
        Probe is a instance subclas inherits
    """
    return (issubclass(type(obj), a_class)) and type(obj) is not a_class
