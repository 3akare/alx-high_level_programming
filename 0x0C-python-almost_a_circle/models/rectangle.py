#!/usr/bin/python3
"""Defines a rectangle class"""
from models.base import Base
# Base = __import__('base').Base


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

    def area(self):
        """
            returns the area value of the Rectangle instance
        """
        return (self.width * self.height)

    def display(self):
        """
            prints to stdout the rectangle instance with the character '#'
        """
        for k in range(self.y):
            print('')
        for i in range(self.height):
            for m in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print('')

    def update(self, *args, **kwargs):
        """
            Update the class Rectangle by adding the public method
        """
        if (args and len(args) != 0):
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif (kwargs and len(kwargs) != 0):
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """
            Overrides the __str__ method
        """
        text = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return (text.format(self.id, self.x, self.y, self.width, self.height))
