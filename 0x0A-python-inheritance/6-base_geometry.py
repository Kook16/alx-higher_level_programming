#!/usr/bin/python3
'''Defining a BaseGeometry class
'''


class BaseGeometry:
    ''' This class raises an execption if area is not implemented
    '''
    def area(self):
        if self.area:
            raise Exception('area() is not implemented')
