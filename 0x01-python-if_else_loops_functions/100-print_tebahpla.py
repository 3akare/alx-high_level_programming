#!/usr/bin/python3
for alpha in range(122, 96, -1):
    if (alpha % 2 != 0):
        alpha = alpha - 32
    print("{}".format(chr(alpha)), end='')
