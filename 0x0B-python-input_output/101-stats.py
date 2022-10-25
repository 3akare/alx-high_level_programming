#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics'''
import sys

o_put = '''File size: {}'''
t_size = 0
num = 10
s_code = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
    }
for ln in sys.stdin:
    if (num == 0):
        print(o_put.format(t_size))
        for k, v in s_code.items():
            if v != 0:
                print(f'{k}: {v}')
        num = 10
    num -= 1
    ln = [ln.split()]
    t_size += int(ln[0][-1])
    s_code[ln[0][-2]] += 1
