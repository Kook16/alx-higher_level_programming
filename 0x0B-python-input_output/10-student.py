#!/usr/bin/python3
'''Defining a Student class
'''


class Student:
    '''Student class defines a student
    '''
    def __init__(self, first_name, last_name, age):
        '''This is the intializer function'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''this function retrieves a dict representation of class instance'''
        if type(attrs) is list and all(type(ele) is str for ele in attrs):
            json_data = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_data[attr] = getattr(self, attr)
            return json_data
        return self.__dict__
