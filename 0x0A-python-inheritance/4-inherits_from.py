#!/usr/bin/python3
"""
Module Name: 4-inherits_from.py
Desc: checks if an object is an inherits from of a class
Function Name: inherits_from()
"""


def inherits_from(obj, a_class):
    """
    inherits_from: checks if obj is an instance of a_class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
