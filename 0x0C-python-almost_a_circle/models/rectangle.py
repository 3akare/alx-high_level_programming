#!/usr/bin/python3
"""Defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """
    Represents the rectangle model that inherits from the Base Model
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Intialize a new rectangle

            Args:
                width(int): the width of the rectangle
                height(int): the height of the rectangle
                x(int): the x coordinate of the rectangle
                y(int): the y coordinate of the rectangle
                id(int): the identity of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if (value <= 0):
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """set/get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if (value <= 0):
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """set/get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        if (value < 0):
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """set/get the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        if (value < 0):
            raise ValueError('y must be >= 0')
        self.__y = value
