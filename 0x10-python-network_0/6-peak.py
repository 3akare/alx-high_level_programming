#!/usr/bin/python3
''' Find peak in a list of unsorted integers '''

def find_peak(list_of_integer):
    ''' FInds the peak in a list of unsorted integers '''
    try:
        for i in range(len(list_of_integer)):
            if (list_of_integer[i - 1] <= list_of_integer[i]) and (list_of_integer[i] >= list_of_integer[i + 1]):
                return (list_of_integer[i])
    except Exception:
        pass


print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))