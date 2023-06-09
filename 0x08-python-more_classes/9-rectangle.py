#!/usr/bin/python3
'''
Defining a Rectangle class
'''


class Rectangle:
    '''
    Rectangle class
    '''
    number_of_instances = 0
    print_symbol = '#'

    @classmethod
    def square(cls, size=0):
        '''
        returns a new Rectangle with width==height==size
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''''
        Returns the biggest rectangle based on the area
        '''
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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

    def area(self):
        '''
        returns the area of the rectangle
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''
        return the perimeter of the rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''
        returns the rectangle with "#"
        '''
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for i in range(self.__height):
            if i is not self.__height - 1:
                rectangle += str(self.print_symbol) * self.__width + '\n'
            else:
                rectangle += str(self.print_symbol) * self.__width
        return rectangle

    def __repr__(self):
        '''
        return the string representation of  the string
        '''
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        '''
        deletes an instance from the class
        '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
