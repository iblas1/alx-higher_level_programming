#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_length = len(sys.argv)
    i = 1
    print("{} arguments:".format(arg_length - 1))
    while i < arg_length:
        print("{}: {}".format(i, sys.argv[i]))
        i = i + 1
