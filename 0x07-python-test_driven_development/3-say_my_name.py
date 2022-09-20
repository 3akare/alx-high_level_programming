#!/usr/bin/python3
"""
    Module Name: 3-say_my_name
    Desc: prints out a formtted text
    Function Name: say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
        prints out a formatted text
    """

    message = "My name is {first} {last}"
    if (not isinstance(first_name, str)):
        raise TypeError('first_name must be a string')
    if (not isinstance(last_name, str)):
        raise TypeError('last_name must be a string')

    print(message.format(first=first_name, last=last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt", verbose=True)
