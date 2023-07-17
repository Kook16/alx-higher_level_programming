#!/usr/bin/python3
'''Defining a Square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''The Square class is a  subclass of Rectangle class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initializes the object attributes'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Gets the value of size'''
        return self.width

    @size.setter
    def size(self, val):
        '''validates val and after assigns it to width'''
        if type(val) is not int:
            raise TypeError('size must be an integer')
        if val <= 0:
            raise ValueError('size must be > 0')
        self.width = val

    def update(self, *args, **kwargs):
        '''Assigns attributes'''
        if args:
            tup = ('id', 'size', 'x', 'y')
            len_tup = len(tup)
            len_args = len(args)
            i = 0
            while i < len_args and i < len_tup:
                setattr(self, tup[i], args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of a Square'''
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }

    def __str__(self):
        '''Return an informal representation of the Square object'''
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'
