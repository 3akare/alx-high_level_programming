#!/usr/bin/python3
"""Defines a text file-writing (appends) function"""


def append_write(filename='', text=''):
    """Write (appends) a text into filename"""
    with open(filename, 'a', encoding='utf-8') as f:
        nb_characters = f.write(text)
    return nb_characters
