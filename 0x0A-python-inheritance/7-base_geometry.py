#!/usr/bin/python3
"""
Module Name: 7-base_geometry.py
Desc: creates an empty class
Class Name: BaseGeometry
"""


class BaseGeometry():
    """
    inherits_from: checks if obj is an instance of a_class
    """
    def area(self):
        """not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        integer_validator: checks if value is an integer
        """

        if not (isinstance(value, int)):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/7-base_geometry.txt', verbose=True)
