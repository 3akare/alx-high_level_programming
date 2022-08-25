#!/usr/bin/python3
def uppercase(str):
    for alpha in str:
        if (ord(alpha) >= 97 and ord(alpha) <= 122):
            alpha = chr(ord(alpha) - 32)
        print('{}'.format(alpha), end='')
    print("")
