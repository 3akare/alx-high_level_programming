#!/usr/bin/python3
def complex_delete(a_dictionary, value=""):
    i = 0
    while (i < len(a_dictionary)):
        for key, val in a_dictionary.items():
            if val == value:
                del a_dictionary[key]
                break
        i += 1
    return a_dictionary
