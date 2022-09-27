#!/usr/bin/python3
"""Defines a text file-writing function"""


def write_file(filename='', text=''):
    """Write a text into filename"""
    with open(filename, 'w', encoding='utf-8') as f:
        nb_characters = f.write(text)
    return nb_characters
