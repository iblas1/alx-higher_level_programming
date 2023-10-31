#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
last_digit = int(str(number)[-1])
last_digit = last_digit * -1 if number < 0 else last_digit
if last_digit > 5:
    print(str1, number, "is", last_digit, "and is greater than 5")
elif last_digit == 0:
    print(str1, number, "is", last_digit, "and is 0")
elif last_digit < 6 and not 0:
    print(str1, number, "is", last_digit, "and is less than 6 and not 0")

