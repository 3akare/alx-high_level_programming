#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('9-rectangle').Rectangle


class Square(BaseGeometry):
    """Represents a rectangle using BaseGeometry."""

    def __init__(self, size):
        """Intialize a new rectangle """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of the rectangle"""
        return self.__size ** 2

    def __str__(self):
        """Return the print() and str() representation of a rectangle"""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__size) + "/" + str(self.__size)
        return string
