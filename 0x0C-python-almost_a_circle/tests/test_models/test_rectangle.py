#!/usr/bin/python3
'''Defining Test_Rectangle class'''
import unittest
from models.rectangle import Rectangle
import io
import sys


class Test_Rectangle(unittest.TestCase):
    '''Tests for the Rectangle class'''

    def setUp(self):
        '''Create objects to be used in all other test cases
'''
        self.r1 = Rectangle(10, 2, 0, 0, 15)
        self.r2 = Rectangle(3, 2, 1, 1, 12)
        self.r = Rectangle(2, 3, 0, 0, 12)
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        '''clears out anything thats not needed after all test are executed'''
        output = self.captured_output.getvalue()
        sys.stdout = sys.__stdout__
        return output

    def test_class_has_docstring(self):
        '''Test if the class has a docstring'''
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertNotEqual(Rectangle.__doc__, "")

    def test_init_docstring(self):
        '''Test if the init method has a docstring'''
        self.assertIsNotNone(self.r1.__init__.__doc__)
        self.assertNotEqual(self.r1.__init__.__doc__, "")

    def test_init_default_values(self):
        '''Test for default values and inheritance from parent'''
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r1.x, 0)

    def test_init_all_values(self):
        '''Test when all the arguments are passes to the Rectangle class'''
        self.assertEqual(self.r2.width, 3)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 1)
        self.assertEqual(self.r2.y, 1)
        self.assertEqual(self.r2.id, 12)

    def test_width_validation_exception_non_int(self):
        '''Test for valid values of width ie only ints'''
        with self.assertRaises(TypeError) as msg:
            r4 = Rectangle('a', 10)
        # check the exception message
        self.assertEqual(str(msg.exception), "width must be an integer")

    def test_width_validation_excet_int_less_1(self):
        '''test for width arguments less than 1'''
        with self.assertRaises(ValueError) as msg:
            r5 = Rectangle(-1, 10)
        # check the exception msg
        self.assertEqual(str(msg.exception), "width must be > 0")

    def test_height_validation_excet_int_type(self):
        '''test for valid type of height is only ints'''
        with self.assertRaises(TypeError) as msg:
            r3 = Rectangle(2, 'h')

        self.assertEqual(str(msg.exception), "height must be an integer")

    def test_height_validation_excet_int_less_1(self):
        '''test for height int value less than 1'''
        with self.assertRaises(ValueError) as msg:
            r6 = Rectangle(1, -10)
        self.assertEqual(str(msg.exception), "height must be > 0")

    def test_x_validation_except_only_int(self):
        '''Test for x type ie only ints required'''
        with self.assertRaises(TypeError) as msg:
            r7 = Rectangle(1, 1, 'c')
        self.assertEqual(str(msg.exception), "x must be an integer")

    def test_x_validation_except_int_less_0(self):
        '''Test for int values of x less than 0'''
        with self.assertRaises(ValueError) as msg:
            r8 = Rectangle(1, 1, -1)

        self.assertEqual(str(msg.exception), "x must be >= 0")

    def test_y_validation_except_only_int(self):
        '''Test for y type ie only ints required'''
        with self.assertRaises(TypeError) as msg:
            r9 = Rectangle(1, 1, 1, 'y')

        self.assertEqual(str(msg.exception), "y must be an integer")

    def test_x_validation_except_int_less_0(self):
        '''Test for int values of x less than 0'''
        with self.assertRaises(ValueError) as msg:
            r10 = Rectangle(1, 1, 3, -1)
        self.assertEqual(str(msg.exception), "y must be >= 0")

    def test_area_docstring(self):
        '''Tests if area method has a docstring'''
        self.assertIsNotNone(self.r1.area().__doc__)
        self.assertNotEqual(self.r1.area().__doc__, "")

    def test_area(self):
        '''Test for area of the rectangle'''
        self.assertEqual(self.r1.area(), 20)

    def test_display_docstring(self):
        '''Tests if area method has a docstring'''
        self.assertIsNotNone(self.r1.display.__doc__)
        self.assertNotEqual(self.r1.display.__doc__, "")

    def test_area_exception(self):
        '''Test for invalid number of arguments passed to area()'''
        with self.assertRaises(TypeError):
            area = self.r1.area(1)

    def test_display(self):
        '''Test the display function'''
        self.r.display()
        expected_output = '##\n##\n##\n'
        self.assertEqual(self.tearDown(), expected_output)

    def test_display_with_x_and_y(self):
        '''Test with values of x and y'''
        self.r2.display()
        expected_output = '\n ###\n ###\n'
        self.assertEqual(self.tearDown(), expected_output)

    def test_display_except(self):
        '''Test display function with invalid argument'''
        with self.assertRaises(TypeError):
            self.r2.display(1)

    def test_str(self):
        '''Test for the __str__ function'''
        self.r.__str__()
        self.assertEqual(self.r.__str__(), "[Rectangle] (12) 0/0 - 2/3")

    def test_str_except(self):
        '''Tests for invalid use of the function'''
        with self.assertRaises(TypeError):
            self.r.__str__(1)

    def test_update_docstring(self):
        '''Tests if area method has a docstring'''
        self.assertIsNotNone(self.r1.update.__doc__)
        self.assertNotEqual(self.r1.update.__doc__, "")

    def test_update_all_arguments(self):
        '''Tests for update with all arguments'''
        self.r1.update(89, 2, 4, 3, 3)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 4)
        self.assertEqual(self.r1.x, 3)
        self.assertEqual(self.r1.y, 3)

    def test_update_with_exces_arguments(self):
        '''Tests for update with all arguments'''
        self.r1.update(89, 2, 4, 3, 3, 9, 1)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 4)
        self.assertEqual(self.r1.x, 3)
        self.assertEqual(self.r1.y, 3)

    def test_update_some_arguments(self):
        '''Test for update function'''
        self.r1.update(89, 2, 3)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

    def test_update_no_arguments(self):
        '''Test for update function with no parameter'''
        self.r1.update()
        self.assertEqual(self.r1.id, 15)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

    def test_update_invalid_argument_width(self):
        "Test for update function with invalid parameter types"
        with self.assertRaises(TypeError) as msg:
            self.r1.update(17, 'a')
        self.assertEqual(str(msg.exception), "width must be an integer")

    def test_update_invalid_argument_height(self):
        "Test for update function with invalid parameter types"
        with self.assertRaises(TypeError) as msg:
            self.r1.update(17, 1, 'h')
        self.assertEqual(str(msg.exception), "height must be an integer")

    def test_update_invalid_argument_x(self):
        "Test for update function with invalid parameter types"
        with self.assertRaises(TypeError) as msg:
            self.r1.update(17, 1, 4, 1.3)
        self.assertEqual(str(msg.exception), "x must be an integer")

    def test_update_invalid_argument_y(self):
        "Test for update function with invalid parameter types"
        with self.assertRaises(TypeError) as msg:
            self.r1.update(17, 1, 3, 2, 'y')
        self.assertEqual(str(msg.exception), "y must be an integer")

    def test_update_invalid_int_value_width(self):
        "Test for update method with invalid int values"
        with self.assertRaises(ValueError) as msg:
            self.r1.update(17, 0, 7)
        self.assertEqual(str(msg.exception), "width must be > 0")

    def test_update_invalid_int_value_height(self):
        "Test for update method with invalid int values"
        with self.assertRaises(ValueError) as msg:
            self.r1.update(17, 7, 0)
        self.assertEqual(str(msg.exception), "height must be > 0")

    def test_update_invalid_int_value_x(self):
        "Test for update method with invalid int values"
        with self.assertRaises(ValueError) as msg:
            self.r1.update(17, 5, 1, -1)
        self.assertEqual(str(msg.exception), "x must be >= 0")

    def test_update_invalid_int_value_y(self):
        "Test for update method with invalid int values"
        with self.assertRaises(ValueError) as msg:
            self.r1.update(17, 5, 1, 1, -1)
        self.assertEqual(str(msg.exception), "y must be >= 0")

    def test_update_args_Kwargs(self):
        '''Test for update method with both args and kwargs'''
        self.r1.update(15, 10, 2, x=1, y=2)
        self.assertEqual(self.r1.id, 15)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

    def test_update_kwargs_only(self):
        self.r1.update(id=19, y=2, width=4, x=3, height=3)
        self.assertEqual(self.r1.id, 19)
        self.assertEqual(self.r1.width, 4)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 3)
        self.assertEqual(self.r1.y, 2)

    def test_update_kwargs_width_invalid(self):
        '''Test for exception caused if width type is not int'''
        with self.assertRaises(TypeError) as msg:
            self.r1.update(id=19, width='a')
        self.assertEqual(str(msg.exception), "width must be an integer")

    def test_update_kwargs_height_invalid(self):
        '''Test for exception caused if width type is not int'''
        with self.assertRaises(TypeError) as msg:
            self.r1.update(id=19, height='a')
        self.assertEqual(str(msg.exception), "height must be an integer")

    def test_update_kwargs_x_invalid(self):
        '''Test for exception caused if x type is not int'''
        with self.assertRaises(TypeError) as msg:
            self.r1.update(id=19, x=12.9)
        self.assertEqual(str(msg.exception), "x must be an integer")

    def test_update_kwargs_width_invalid(self):
        '''Test for exception caused if y type is not intt'''
        with self.assertRaises(TypeError) as msg:
            self.r1.update(id=19, y='ab')
        self.assertEqual(str(msg.exception), "y must be an integer")

    def test_update_kwargs_width_invalid_int_values(self):
        '''Test for exception caused if width is less than 1'''
        with self.assertRaises(ValueError) as msg:
            self.r1.update(id=19, width=-3, height=4)
        self.assertEqual(str(msg.exception), "width must be > 0")

    def test_update_kwargs_height_invalid_int_values(self):
        '''Test for exception caused if width is less than 1'''
        with self.assertRaises(ValueError) as msg:
            self.r1.update(id=19, width=3, height=-4)
        self.assertEqual(str(msg.exception), "height must be > 0")

    def test_update_kwargs_width_invalid_int_values(self):
        '''Test for exception caused if x is less than 1'''
        with self.assertRaises(ValueError) as msg:
            self.r1.update(id=19, width=3, height=4, x=-1)
        self.assertEqual(str(msg.exception), "x must be >= 0")

    def test_update_kwargs_width_invalid_int_values(self):
        '''Test for exception caused if y is less than 1'''
        with self.assertRaises(ValueError) as msg:
            self.r1.update(id=19, width=3, height=4, x=1, y=-7)
        self.assertEqual(str(msg.exception), "y must be >= 0")
