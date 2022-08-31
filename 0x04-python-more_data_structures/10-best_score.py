#!/usr/bin/python3
def best_score(a_dictionary):
    dict_list = []
    max_number = 0
    if isinstance(a_dictionary, dict):
        for value in a_dictionary.values():
            if isinstance(value, int):
                dict_list.append(value)
        max_number = max_integer(dict_list)
        for key, value in a_dictionary.items():
            if max_number == value:
                return key
    else:
        return None
def max_integer(my_list=[]):
    if isinstance(my_list, list):
        if len(my_list) == 0:
            return None
        my_list = sorted(my_list)
        Len = len(my_list)
        return my_list[Len - 1]
    return None