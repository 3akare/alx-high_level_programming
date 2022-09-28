#!/usr/bin/python3
"""Define class"""


class MagicClass:
    """Represents a magic class"""

    def __init__(self, radius=0):
        """intialize a new instance"""
        self.__radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ Area Function """
        return ((3.141592653589793) * (self.__radius ** 2))

    def circumference(self):
        """ Circumference Function """
        return (2 * (3.141592653589793) * (self.__radius))
