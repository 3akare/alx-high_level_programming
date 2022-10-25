#!/usr/bin/python3
'''  inserts a line of text to a file, after each
line containing a specific string '''


def append_after(filename='', search_string='', new_string=''):
    """append a text into filename"""

    with open(filename, 'r', encoding='utf-8') as f:
        string = f.readlines()

    i = 0
    while i < len(string):
        if search_string in string[i]:
            string[i:i + 1] = [string[i], new_string]
            i += 1
        i += 1

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(list_string)
