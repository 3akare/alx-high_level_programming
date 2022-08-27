#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    LenOfList = len(my_list)
    for i in range(LenOfList):
        print("{}".format(my_list[(LenOfList - 1) - i]))
