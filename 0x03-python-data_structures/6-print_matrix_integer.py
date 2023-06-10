#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for item in matrix:
        i = 0
        for item1 in item:
            if i != len(item) -1:
                print('{:d} '.format(item1), end='')
                i += 1
            else:
                print('{:d}'.format(item1), end='')
        print()
