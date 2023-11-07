#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            space = " " if j != len(matrix[i]) - 1 else ""
            print("{:d}".format(matrix[i][j]), end=space)
            j += 1
        i += 1
        print()
