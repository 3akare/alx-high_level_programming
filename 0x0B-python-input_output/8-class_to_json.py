#!/usr/bin/python3
''' returns the dictionary description with 
simple data structure (list, dictionary, string, integer and boolean) 
for JSON serialization of an object '''

import json

def class_to_json(obj):
    '''returns dict description of obj'''
    obj_dict = {}
    if hasattr(obj, '__dict__'):
        return obj.__dict__.copy()
    return obj_dict
