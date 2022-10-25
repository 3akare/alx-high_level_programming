#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics'''
import sys

opt = '''File size: {}'''
t_s = 0
num = 10
s_c = {
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
        print(opt.format(t_s))
        for k, v in s_c.items():
            print(f'{k}: {v}')
        num = 10
    num -= 1
    ln = [ln.split()]
    t_s += int(ln[0][-1])
    s_c[ln[0][-2]] += 1
