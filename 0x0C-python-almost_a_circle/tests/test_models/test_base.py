#!/usr/bin/python3
'''Defining a TestBase class'''
import unittest
import os

from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    '''TestBase provides tests for Base class'''

    def test_class_docstring(self):
        '''Tests class for doctsring'''
        self.assertIsNotNone(Base.__doc__)
        self.assertNotEqual(Base.__doc__, "")

    def test_init_docstring(self):
        '''Tests init method for docstring'''
        b = Base(10)
        self.assertIsNotNone(b.__init__.__doc__)
        self.assertNotEqual(b.__init__.__doc__, "")

    def test_init_default_id(self):
        '''Does Base class handle no arguments passed to it'''
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_init_id_value(self):
        '''Does Base class handle arguments passed to it'''
        b1 = Base(79)
        self.assertEqual(b1.id, 79)

    def test_init_id_values_many_objects(self):
        '''Does Base class work well with many objects with either no\
        arguments or with an argument passed to it'''
        b1 = Base()
        b2 = Base(41)
        b3 = Base()
        b4 = Base(29)
        b5 = Base(12.1)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 41)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 29)
        self.assertEqual(b5.id, 12.1)

    def test_init_with_excess_arguments(self):
        '''Does the Base class take more than one argument'''
        with self.assertRaises(TypeError):
            b7 = Base(12, 17)
