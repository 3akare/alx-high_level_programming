#!/usr/bin/python3
'''
Module Name: 101-lazy_matrix_mul.py
Desc: multiples 2 matrices using numpy
Function Name: lazy_matrix_mul(m_a, m_b)
'''
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''
    Multiples two matrices

    Args:
        m_a - first matrix
        m_b - second matrix
    Returns:
        Multiplication of m_a and m_b with numpy
    '''
    return (np.matmul(m_a, m_b))


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/101-lazy_matrix_mul.txt')
