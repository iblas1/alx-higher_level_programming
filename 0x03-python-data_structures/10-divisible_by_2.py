#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    created_list = []
    for j in range(len(my_list)):
        if my_list[j] % 2 == 0:
            created_list.append(True)
        else:
            created_list.append(False)
    return created_list