#!/usr/bin/python3
"""Define class"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """
            Intailize a new square
            Args:
                size(int): size of a new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            Area Function
            Args:
                self: an instance of Square
            Return: the square of self.__size
        """
        return (self.__size**2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
