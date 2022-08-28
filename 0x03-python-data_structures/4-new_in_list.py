#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > 0 or idx < len(new_list):
        new_list = [x for x in my_list]
        new_list[idx] = element
        return new_list
    return my_list
