#!/usr/bin/python3
import sys
lenOfArgv = (len(sys.argv) - 1)
index = 1
if ((lenOfArgv == 0)):
    print(f'{lenOfArgv} arguments.')
else:
    if (lenOfArgv == 1):
        print(f'{lenOfArgv} argument:')
        print(f'{lenOfArgv}: {sys.argv[lenOfArgv]}')
    else:
        print(f'{lenOfArgv} arguments:')
        while (index < (lenOfArgv + 1)):
            print(f'{index}: {sys.argv[index]}')
            index += 1
