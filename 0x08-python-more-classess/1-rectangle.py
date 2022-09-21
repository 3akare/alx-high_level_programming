#!/usr/bin/python3
"""Define a class"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """
            Intailize a new rectangle
            Args:
                width(int): width of new rectangle
                height(int): height of new rectangle
        """
        if (not isinstance(width, int)):
            raise TypeError('width must be an integer')
        if (width < 0):
            raise ValueError('width must be >= 0')
        if (not isinstance(height, int)):
            raise TypeError('height must be an integer')
        if (height < 0):
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            elif value < 0:
                raise TypeError('height must be >= 0')
            self.__height = value

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            elif value < 0:
                raise TypeError('width must be >= 0')
            self.__width = value
