#!/usr/bin/python3
''' Define Student Class '''


class Student:
    def __init__(self, first_name, last_name, age):
        '''Student init'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
            retrieves a dictionary represntation of a Student instance
        '''
        obj_dict = {}
        if hasattr(self, '__dict__'):
            return self.__dict__.copy()
        return obj_dict
