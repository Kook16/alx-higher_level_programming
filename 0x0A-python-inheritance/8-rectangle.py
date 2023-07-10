#!/usr/bin/python3
'''Defining a Rectangle class that inherits from BaseGeometry class
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Rectangle class is a subclass of BaseGeometry
    '''
    def __init__(self, width, height):
        ''' This is initializer function
        '''
        if self.integer_validator('width', width):
            self._width = width
        if self.integer_validator('height', height):
            self._height = height
