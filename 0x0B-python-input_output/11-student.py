#!/usr/bin/python3
"""fhjkk"""


class Student:
    def __init__(self, first_name, last_name, age):
        """dhjkk"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dgjjk"""
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict

    def reload_from_json(self, json):
        """fhjk"""
        for key, value in json.items():
            setattr(self, key, value)
