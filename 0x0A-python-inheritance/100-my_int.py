#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """Invert the int operators"""

    def __eq__(self, other):
        """equal to"""

        return (self.real != other)

    def __ne__(self, other):
        """not equal to"""

        return self.real == other
