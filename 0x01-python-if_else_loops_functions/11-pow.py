#!/usr/bin/python3
def pow(a, b):
    result  = 1
    if b < 0:
        while b < 0:
            result = result * a
            b = b + 1
    else:
        while b > 0:
            result = result * a
            b = b - 1
    return  result
    

print(pow(-5, 2))