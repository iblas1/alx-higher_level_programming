#!/usr/bin/python3
def no_c(my_string):
    i = 0
    new_string = ""
    lower_str = my_string.lower()
    string_length = len(lower_str)
    while i < string_length:
        if lower_str[i] == 'c':
            i += 1
            continue
        new_string += my_string[i]
        i = i + 1
    return new_string
