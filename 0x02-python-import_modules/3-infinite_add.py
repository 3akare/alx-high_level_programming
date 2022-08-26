#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    total = 0
    index = 1
    while (index < len(sys.argv)):
        numbers = int(sys.argv[index])
        total += numbers
        index += 1
    print("{}".format(total))
