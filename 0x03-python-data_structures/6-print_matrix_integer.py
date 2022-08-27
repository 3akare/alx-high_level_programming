#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    j = 0
    while (j < len(matrix)):
        for i in range(len(matrix[j])):
            print("{:d}".format(matrix[j][i]), end='')
            if i != (len(matrix[i]) - 1):
                print(" ", end="")
        print("")
        j += 1
