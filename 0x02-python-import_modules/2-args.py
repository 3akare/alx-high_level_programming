#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    LenOfArgv = (len(sys.argv) - 1)
    index = 1
    if LenOfArgv == 0:
        print("{} arguments.".format(LenOfArgv))
    else:
        if LenOfArgv == 1:
            print("{} argument:".format(LenOfArgv))
            print("{}: {}".format(LenOfArgv, sys.argv[LenOfArgv]))
        else:
            print("{} arguments:".format(LenOfArgv))
            while (index < (LenOfArgv + 1)):
                print("{}: {}".format(index, sys.argv[index]))
                index += 1
