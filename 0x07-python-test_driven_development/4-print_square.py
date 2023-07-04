#!/usr/bin/python3
'''
defining print_square function
'''


def print_square(size):
    '''
    print_square - prints a square with the character #
    Args:
        size: length of the square in integer
    Return:
        Returns nothing
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
