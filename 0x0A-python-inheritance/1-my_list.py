#!/usr/bin/python3
"""
Module Name: 1-my_list.py
Desc: defines a class that inherits from list
class name: Mylist
"""


class MyList(list):
    """
    Mylist: inherits from list object
    """
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/1-my_list.txt', verbose=True)
