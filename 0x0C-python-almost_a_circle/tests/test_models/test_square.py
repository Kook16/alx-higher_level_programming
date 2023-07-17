#!/usr/bin/python3
'''Defining a Square class'''
import unittest
from models.square import Square


class Test_Square(unittest.TestCase):
    '''Test_Square contains tests for the Square class'''

    def setUp(self):
        '''Creates objects that are avaiable in all other tests'''
        self.s1 = Square(5)
        self.s2 = Square(2, 2)
        self.s3 = Square(3, 1, 3)

    def test_class_docstring(self):
        '''Tests class for docstring'''
        self.assertIsNotNone(Square.__doc__)
        self.assertNotEqual(Square.__doc__, "")

    def test_init_docstring(self):
        '''Tests init method for docstring'''
        self.assertIsNotNone(self.s1.__init__.__doc__)
        self.assertNotEqual(self.s1.__init__.__doc__, "")
