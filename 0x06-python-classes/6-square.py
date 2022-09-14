#!/usr/bin/python3
"""Define class"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
            Intailize a new square
            Args:
                size(int): size of a new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__position = value

    def my_print(self):
        """ prints out a square to stdout"""
        if (self.__size == 0):
            pass
        else:
            if (self.__position[1] > 0):
                print("")
            else:
                for k in range(self.__position[1]):
                    print(" ")

            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("{}".format('#'), end="")
                print("")
