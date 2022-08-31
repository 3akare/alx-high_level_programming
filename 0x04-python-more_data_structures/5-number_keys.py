#!/usr/bin/python3
def number_keys(a_dictonary):
    keys = 0
    for key in a_dictonary.keys():
        if key:
            keys += 1
    return keys
