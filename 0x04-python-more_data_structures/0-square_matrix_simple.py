#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    matrix_copy = []
    for item in matrix:
        matrix_copy.append(item[:])
    for item in matrix_copy:
        for index in range(len(item)):
            item[index] **= 2
    return matrix_copy
