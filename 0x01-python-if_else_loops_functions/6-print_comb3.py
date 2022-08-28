#!/usr/bin/python3
i = 0
j = 0
while (i <= 9):
    j = i + 1
    while (j <= 9):
        if (j == 9 and i == 8):
            print("{}{}".format(i, j))
            break
        print("{}{}".format(i, j), end=", ")
        j = j + 1
    i = i + 1
