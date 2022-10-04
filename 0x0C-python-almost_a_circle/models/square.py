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

    def update(self, *args, **kwargs):
        """
            Update the class square by adding the public method
        """
        if (args and len(args) != 0):
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif (kwargs and len(kwargs) != 0):
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
