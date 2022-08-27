#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    Len = len(my_list)
    for i in range(0, Len):
        print("{:d}".format(my_list[(Len - 1) - i]))
