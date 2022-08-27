#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    Len = len(my_list)
    for i in range(0, Len):
        print(my_list[(Len - 1) - i])

print_reversed_list_integer([[1, 2, 3], [4, 5, 6], [7, 8, 9]])