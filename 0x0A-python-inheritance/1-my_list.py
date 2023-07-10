#!/usr/bin/python3
'''Defining a class MyList that inherits from a list
'''


class MyList(list):
    ''' MyList class inherits from a list
    '''
    def __init__(self):
        '''This is the initializer function
        '''
        super().__init__()

    def print_sorted(self):
        '''Prints the list but in ascending order
        '''
        print(sorted(self))
