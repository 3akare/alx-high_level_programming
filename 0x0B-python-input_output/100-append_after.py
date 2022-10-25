#!/usr/bin/python3
'''  inserts a line of text to a file, after each
line containing a specific string '''


def append_after(filename='', search_string='', new_string=''):
    """append a text into filename"""

    with open(filename, 'r', encoding='utf-8') as f:
        string = f.readlines()
        f.close

    num = 0
    list_string = string[:]
    for i in string:
        if (search_string in i):
            num += 1
            idx = string.index(i)
            list_string.insert(idx + num, new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(list_string)
        f.close
