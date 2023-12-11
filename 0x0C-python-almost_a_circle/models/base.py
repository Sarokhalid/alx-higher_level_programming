#!/usr/bin/python3
'''module for base class'''
import json


class Base:
    '''represent base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''gwhdjhujeqifhdhjekjkw'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''hdjhwehgdjwdiwiudhhwgjduwo'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''ghsdjkikk'''
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        json_string = cls.to_json_string([obj.to_dictionary()
                                          for obj in list_objs])
        with open(filename, "w") as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''hjkwjdhhjwd'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        '''kjfkjdjfkdkgfakd'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
