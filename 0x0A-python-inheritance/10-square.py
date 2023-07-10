#!/usr/bin/python3
''' Defining Square class that inherits from subclass Rectangel
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square class that implement the area of a square
    '''
    def __init__(self, size):
        '''Initializes the size'''
        self.integer_validator('size', size)
        self._size = size

    def area(self):
        '''Computes the area of square'''
        return self._size ** 2

    def __str__(self):
        return f'[Rectangle] {self._size}/{self._size}'
