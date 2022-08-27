#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    j = 0
    while (j < len(matrix)):
        for i in range(0, len(matrix[j])):
            print("{:d}".format(matrix[j][i]), end=' ')
        print("")
        j += 1
