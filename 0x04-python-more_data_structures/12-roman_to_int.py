#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    sum = 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    for i in range(0, len(roman_string)):
        if (roman_dict.get(roman_string[i], 0) == 0):
            return 0
        if (i != len(roman_string) - 1) and roman_dict.get(roman_string[i])\
                < roman_dict.get(roman_string[i + 1]):
            sum += roman_dict.get(roman_string[i]) * -1
        else:
            sum += roman_dict.get(roman_string[i])
    return sum
