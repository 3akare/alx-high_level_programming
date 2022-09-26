#!/usr/bin/python3
"""
Module Name: 3-is_kind_of_class.py
Desc: checks if an object is an instance of a class
Function Name: is_kind_of_class()
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class: checks if obj is an instance of a_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
