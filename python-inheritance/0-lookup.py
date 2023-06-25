#!/usr/bin/python3
"""lookup = __import__('0-lookup').lookup"""


def lookup(obj):
    """function that returns the list of
    available attributes and methods of an object"""
    return list(dir(obj))
