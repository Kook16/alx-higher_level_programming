#!/usr/bin/python3
'''
A square class
'''


class Square:
    '''__init__ function'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''size function'''
        return self.__size

    @property
    def position(self):
        '''position function'''
        return self.__position

    @size.setter
    def size(self, value):
        '''size function'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        '''position function'''
        if (len(position) != 2 or
            not instance(value, tuple) or
            value[0] < 0 or
            value[1] < 0 or
            type(position[1]) != int or
            type(position[0]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        ''' area function '''
        return self.__size ** 2

    def my_print(self):
        '''print function'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
