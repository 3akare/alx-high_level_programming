#!/usr/bin/python3
"""Defines a Square class"""
from models.rectangle import Rectangle
# Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """
    Represents the square model that inherits from the rectangle Model
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Intialize a new rectangle

            Args:
                size(int): the size of the square
                x(int): the x coordinate of the square
                y(int): the y coordinate of the square
                id(int): the identity of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """set/get the width of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
            Overrides the __str__ method
        """
        text = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return (text.format(self.id, self.x, self.y, self.width))
