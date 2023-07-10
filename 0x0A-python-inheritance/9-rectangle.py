#!/usr/bin/python3
'''Definig Rectangle which is subclass of BaseGeometry
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Rectangle class is a subclass of BaseGeometry
    '''
    def __init__(self, width, height):
        ''' This is initializer function
        '''
        self.integer_validator('width', width)
        self._width = width
        self.integer_validator('height', height)
        self._height = height

    def area(self):
        '''Computes the area of the rectangle
        '''
        return self._width * self._height

    def __str__(self):
        '''Returns an informal representation of the object
        '''
        return f'[Rectangle] {self._width}/{self._height}'
