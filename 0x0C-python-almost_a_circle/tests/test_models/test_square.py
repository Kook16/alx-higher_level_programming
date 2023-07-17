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

    def test_init_(self):
        '''Tests the init values'''
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s1.id, 14)

    def test_init_invalid_type_size(self):
        '''checks if size is not int'''
        with self.assertRaises(TypeError) as msg:
            s1 = Square('a')
        self.assertEqual(str(msg.exception), "width must be an integer")

    def test_init_invalid_type_x(self):
        '''checks if x is not int'''
        with self.assertRaises(TypeError) as msg:
            s1 = Square(4, 'a')
        self.assertEqual(str(msg.exception), "x must be \
an integer")

    def test_init_invalid_type_y(self):
        '''checks if size is not int'''
        with self.assertRaises(TypeError) as msg:
             s1 = Square(3, 4, 'a')
        self.assertEqual(str(msg.exception), "y must be \
an integer")

    def test_init_value_size(self):
        '''checks if size is not int'''
        with self.assertRaises(ValueError) as msg:
            s1 = Square(-1)
        self.assertEqual(str(msg.exception), "width must be > 0")

    def test_init_value_x(self):
        '''checks if size is not int'''
        with self.assertRaises(ValueError) as msg:
            s1 = Square(2, -1)
        self.assertEqual(str(msg.exception), "x must be \
>= 0")

    def test_init_value_y(self):
        '''checks if size is not int'''
        with self.assertRaises(ValueError) as msg:
             s1 = Square(2, 0, -1)
        self.assertEqual(str(msg.exception), "y must be \
>= 0")
