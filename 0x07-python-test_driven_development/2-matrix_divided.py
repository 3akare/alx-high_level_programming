#!/usr/bin/python3
"""
Module Name: 2-matrix_divided.py
Desc: defines a function that divides all elements of a matrix
Function Name: matrix_divided
"""


def matrix_divided(matrix, div):
    """
    matix_divided: divides all the elements of a matrix
    """

    message = 'matrix must be a matrix (list of lists) of integers/floats'
    if (not isinstance(matrix, list) or matrix == [] or
            not all((isinstance(n, list) for n in matrix)) or
            not all((isinstance(k, int) or isinstance(k, float))
                    for k in [num for row in matrix for num in row])):
        raise TypeError(message)

    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError('div must be a number')
    if (not (all((len(n) == len(matrix[0])) for n in matrix))):
        raise TypeError('Each row of the matrix must have the same size')
    if (div == 0):
        raise ZeroDivisionError('division by zero')

    j = 0
    new_matrix = [row[:] for row in matrix]
    while (j < len(new_matrix)):
        for i in range(len(new_matrix[j])):
            new_matrix[j][i] = new_matrix[j][i] / div
            new_matrix[j][i] = round(new_matrix[j][i], 2)
        j += 1
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt', verbose=True)
