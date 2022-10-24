#!/usr/bin/python3
'''Pascal's Triangle'''


def pascal_triangle(n):
    """pascal triangle"""
    new_list = []
    line = [1]
    y = [0]
    for x in range(max(n, 0)):
        new_list.append(line)
        line = [lp + r for lp, r in zip(line + y, y + line)]
    return new_list
