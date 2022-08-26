#!/usr/bin/python3
import sys
lenOfArgv = (len(sys.argv) - 1)
index = 1
if ((lenOfArgv == 0)):
    print("{} arguments.".format(lenOfArgv))
else:
    if (lenOfArgv == 1):
        print("{} argument:".format(lenOfArgv))
        print("{}: {}".format(lenOfArgv, sys.argv[lenOfArgv]))
    else:
        print("{} arguments:". format(lenOfArgv))
        while (index < (lenOfArgv + 1)):
            print("{}: {}".format(index, sys.argv[index]))
            index += 1
