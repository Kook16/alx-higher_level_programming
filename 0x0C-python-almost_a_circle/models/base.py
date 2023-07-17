#!/usr/bin/python3
'''Defining a Base class'''
import json


class Base:
    ''' Base class'''
    __nb_objects = 0

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        '''that returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file
        Args:
            list_objs: is a list of instances who inherits of Base\
        - example: list of Rectangle or list of Square instances
        '''
        file_name = cls.__name__ + '.json'
        list_dict = []
        with open(file_name, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                for obj in list_objs:
                    obj_dict = obj.to_dictionary()
                    list_dict.append(obj_dict)
                f.write(cls.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set'''
        if dictionary is not None:
            if cls.__name__ == "Rectangle":
                inst = cls(2, 4)
            if cls.__name__ == "Square":
                inst = cls(4)
            inst.update(**dictionary)
            return inst

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name) as f:
                data = Base.from_json_string(f.read())
            result = []
            for item in data:
                instance = cls.create(**item)
                result.append(instance)
            return result
        except FileNotFoundError:
            return []

    def __init__(self, id=None):
        '''Initializer function'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
