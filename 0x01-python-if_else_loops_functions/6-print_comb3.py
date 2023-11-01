#!/usr/bin/python3
for first_digit in range(10):
    for second_digit in range(first_digit + 1, 10):
        if first_digit == 9 and second_digit == 8:
            print("{:02d}".format(first_digit * 10 + second_digit))
        else:
            print("{:02d}".format(first_digit * 10 + second_digit), end=', ')
print()
