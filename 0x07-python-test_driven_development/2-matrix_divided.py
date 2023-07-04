#!/usr/bin/pyhton3
'''
Defining a matrix_divided function
'''


def matrix_divided(matrix, div):
    '''
    matrix_divided - function that divides all elements of a matrix

    args:
        matrix: This is a 2D list
        div: The value that is used to divide the matrix
    Return:
         A new matrix that is divided
    '''
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if len(matrix) == 0:
        return matrix
    for items in matrix:
        for item in items:
            if type(item) is not int and type(item) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of"
                                " integers/floats")
    row_len = len(matrix[0])
    for items in matrix:
        if row_len is not len(items):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    copy = []
    for items in matrix:
        sub_copy = []
        for item in items:
            sub_copy.append(item)
        copy.append(sub_copy)
    for items in copy:
        for i in range(0, len(items)):
            items[i] /= div
            items[i] = round(items[i], 2)
    return copy
