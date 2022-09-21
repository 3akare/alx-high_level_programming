#!/usr/bin/python3
"""
Module Name: 0-add_integer.py
Desc: defines as integer addition function
Function name: add_integer()
"""


def add_integer(a, b=98):
    """
    add_integer: adds integers and returns the sum
    """
    if (a == float('inf')):
        raise OverflowError("cannot convert float infinity to integer")
    if (a == float('NaN')):
        raise ValueError("cannot convert float NaN to integer")
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return (a + b)


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/0-add_integer.txt', verbose=True)
