#!/usr/bin/python3
"""
Module Name: 2-is_same_class.py
Desc: checks if an object is exactly an instance of a specified class
Function Name: is_same_class()
"""


def is_same_class(obj, a_class):
    """
    is_same_class: checks if obj is an instance of a_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
