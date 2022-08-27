#!/usr/bin/python3
from turtle import clear


def max_integer(my_list=[]):
    if len(my_list) < 0:
        return None
    my_list = sorted(my_list)
    Len = len(my_list)
    return my_list[Len - 1]
