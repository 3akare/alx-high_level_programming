#!/usr/bin/python3
"""Defines a text file-reading function"""


def read_file(filename=""):
    """Prints the content of filename to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
