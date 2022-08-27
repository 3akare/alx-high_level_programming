#!/usr/bin/python3
def print_list_integer(my_list=[]):
    index = 0
    while (index < len(my_list)):
        print("{:d}".format(my_list[index]))
        index += 1
