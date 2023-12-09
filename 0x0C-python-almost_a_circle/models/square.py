#!/usr/bin/python3
'''ndjkhsfdhjwfhwyfyuwf'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''jajndfdfhgjhbfhf'''
    def __init__(self, size, x=0, y=0, id=None):
        '''udhuiehfhgefwgfhiwhfuiwehf'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''nxcjjsfhuqegbfgwjfhuweofio'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''hcjjdjcjhjckjedjc'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''hqejdjwdhqhjh'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''hwdjhdghidgbudh'''
        if args:
            self.__update(*args)
        elif kwargs:
            self .__update(**kwargs)

    def to_dictionary(self):
        '''hideihiufqhygdhgdyueqgeddgdghg'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
