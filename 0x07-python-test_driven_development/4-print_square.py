#!/usr/bin/python3
"""
Module Name: 4-print_square.py
Desc: prints a square using the hash character '#'
Function Name; print_square
"""


def print_square(size):
    """
        prints a square using the hash character '#'
    """

    if (not isinstance(size, int)):
        raise TypeError('size must be an integer')
    if (size < 0):
        raise ValueError('size must be >= 0')
    if (isinstance(size, float) and size < 0):
        raise TypeError('size must be integer')
    if size == 0:
        print("", end="")
    else:
        for i in range(size):
            for j in range(size):
                print('#', end="")
            print("")


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/4-print_square.txt', verbose=True)
