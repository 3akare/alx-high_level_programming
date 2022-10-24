#!/usr/bin/python3
'''Pascal's Triangle'''

def pascal_triangle(n):
    """to make this tri"""
    tri = []
    line = [1]
    y = [0]
    for x in range(max(n, 0)):
        tri.append(line)
        line = [l + r for l, r in zip(line + y, y + line)]
    return tri
