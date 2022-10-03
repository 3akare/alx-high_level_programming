#!/usr/bin/python3
"""Defines a rectangle class"""
Base = __import__('base').Base


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
        self.__width = value

    @property
    """set/get the height of the rectangle"""
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    """set/get the x coordinate of the rectangle"""
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    """set/get the y coordinate of the rectangle"""
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
