#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_1 = list(set_1)
    set_2 = list(set_2)
    new_list = []
    for i in range(len(set_1)):
        for j in range(len(set_2)):
            if (set_1[i] == set_2[j]):
                new_list.append(set_2[j])
    return set(new_list)
