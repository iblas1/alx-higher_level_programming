#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_length = len(sys.argv)
    i = 1
    result = 0
    while i < arg_length:
        result += int(sys.argv[i])
        i = i + 1
    print("{}".format(result))
