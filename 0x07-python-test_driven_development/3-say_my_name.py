#!/usr/bin/python3
'''
Defining say_my_name function
'''


def say_my_name(first_name, last_name=""):
    '''
    say_my_name - prints prints a message
    Args:
         first_name: A string representing the first name
         last_name: A string representing last name
    Return:
          Nothing
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name} ")
