#!/usr/bin/python3
'''Unittest for max_integer([..])'''

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Test an orderd list
    '''
    def test_ordered_list(self):
        '''Test an ordered list [1, 2, 3, 4]
        '''
        self.assertTrue(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        '''Test unordered list [1, 3, 5, 0]
        '''
        self.assertTrue(max_integer([1, 3, 5, 0]), 5)

    def test_empty_list(self):
        '''Test empty list []
        '''
        self.assertEqual(max_integer([]), None)

    def test_list_with_1_item(self):
        '''Test list with 1 element
        '''
        self.assertTrue(max_integer([5]), 5)

    def test_list_with_float_int(self):
        '''Test list with floats and int
        '''
        self.assertTrue(max_integer([1, 2.5, 7.9, 9]), 9)

    def test_with_string(self):
        '''Test with a string 'hello'
        '''
        self.assertTrue(max_integer('hello'), 'o')

    def test_with_strings(self):
        '''Test list with strings ['hi', 'bye', 'as']
        '''
        self.assertTrue(max_integer(['hi', 'bye', 'as']), 'bye')
