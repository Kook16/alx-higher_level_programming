#!/usr/bin/python3
'''
Defining a Rectangle class
'''


class Rectangle:
    '''
    An empyty class
    '''
    def __init__(self, width=0, height=0):
        '''
        initiailization function
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''
        returns the value of width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        sets the value of width
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        returns the value of width
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        sets the value of height
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
