#!/usr/bin/python3
def uppercase(s):
    for letter in s:
        if 'a' <= letter <= 'z':
            uppercase_char = chr(ord(letter) - 32)
        else:
            uppercase_char = letter
        print(uppercase_char, end='')
    print()
