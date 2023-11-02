#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_length = len(sys.argv)
    i = 1
    if arg_length == 1:
        print("0 arguments.")
    elif arg_length == 2:
        print("1 argument:")
        print("1:", sys.argv[1])
    else:
        print("{} arguments:".format(arg_length - 1))
        while i < arg_length:
            print("{}: {}".format(i, sys.argv[i]))
            i = i + 1
