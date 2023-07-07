#!/usr/bin/python3
'''
Defining add function
'''


def add_integer(a, b=98):
    '''
    add_integer - adds two intgers or floats

    Args:
         a: should be int or flaot
         b: should be int or flaot
    Returns:
         An int which is a sum of a and b
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
