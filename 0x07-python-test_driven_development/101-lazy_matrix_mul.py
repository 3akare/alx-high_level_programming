#!/usr/bin/python3
import numpy as np
"""
Module Name: 101-lazy_matrix_mul.py
Desc: multiples 2 matrices with numpy
Function Name: lazy_matrix_mul(m_a, m_b)
"""


def lazy_matrix_mul(m_a, m_b):
    return(np.matmul(m_a, m_b))

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/101-lazy_matrix_mul.txt')