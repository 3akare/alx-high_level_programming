#!/usr/bin/python3
def element_at(my_list, idx):
    if ((idx < 0)) or ((idx > len(my_list))):
        return None
    index = 0
    while (index < len(my_list)):
        if (index == idx):
            return my_list[index]
        index += 1
