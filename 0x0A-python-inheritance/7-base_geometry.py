#!/usr/bin/python3
'''Defining a BaseGeometry class
'''


class BaseGeometry:
    ''' This class raises an execption if area is not implemented
    '''
    def area(self):
        '''defining an oject method which calculates the area
        '''
        if self.area:
            raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        ''' Function that validates value
        '''
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{str(name)} must be greater than 0')
