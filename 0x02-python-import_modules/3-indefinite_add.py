#!/usr/bin/python3
import sys
sum = 0
index = 1
while (index < len(sys.argv)):
    numbers = int(sys.argv[index])
    sum += numbers
    index += 1
print(f'{sum}')
