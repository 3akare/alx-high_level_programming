#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        max_number, position = 0, 0
        keys_list = list(a_dictionary.keys())
        val_list = list(a_dictionary.values())
        for value in a_dictionary.values():
            if isinstance(value, int):
                if value > max_number:
                    max_number = value
        position = val_list.index(max_number)
        return keys_list[position]
    return None
