#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx in range(len(row)):
            if idx != 0:
                print(" ", end="")
            print("{:d}".format(row[idx]), end="")
        print()
