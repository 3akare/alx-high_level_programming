#!/usr/bin/python3
"""Reads from standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

if __name__ == '__main__':
    import sys

    o_put = '''File size: {}'''
    t_size = 0
    num = 0
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
    try:
        for ln in sys.stdin:
            if (num == 10):
                print(o_put.format(t_size))
                for k, v in s_code.items():
                    if v != 0:
                        print(f'{k}: {v}')
                num = 1
            else:
                num += 1

            ln = [ln.split()]
            try:
                t_size += int(ln[0][-1])
            except (IndexError, ValueError):
                pass

            try:
                s_code[ln[0][-2]] += 1
            except Exception:
                pass
        print(o_put.format(t_size))
        for k, v in s_code.items():
            if v != 0:
                print(f'{k}: {v}')

    except KeyboardInterrupt:
        print(o_put.format(t_size))
        for k, v in s_code.items():
            if v != 0:
                print(f'{k}: {v}')
        raise
