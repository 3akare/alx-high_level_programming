#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator = 0
    deminator = 0
    for i, j in my_list:
        numerator += (i * j)
        deminator += j
    return (numerator/deminator)
