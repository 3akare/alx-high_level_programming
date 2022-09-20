#!/usr/bin/python3
"""
Module Name: 5-text_indentation.py
Desc: prints a text and prints a newline after each of these character: ., ?, :
Function name: text_indentation(text)
"""


def text_indentation(text):
    """
    text_indentation: Desc: prints a text and prints a newline after
    each of these character: ., ?, :"""

    if (not isinstance(text, str)):
        raise TypeError('text must be a string')
    c = 0
    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt", verbose=True)
