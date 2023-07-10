#!/usr/bin/python3
'''Definig is_same_class function
'''


def is_same_class(obj, a_class):
    ''' Returns True if the object is exactly an instance of
    of the specified class, otherwise false
    '''
    if type(obj) == a_class:
        return True
    return False
