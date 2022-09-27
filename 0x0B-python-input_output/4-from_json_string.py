#!/usr/bin/python3
"""Defines a JSON_to_string function"""
import json


def from_json_string(my_str):
    """Returns the string object representation of JSON"""
    return (json.loads(my_str))
