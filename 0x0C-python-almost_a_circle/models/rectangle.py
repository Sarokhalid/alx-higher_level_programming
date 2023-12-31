#!/usr/bin/python3
'''hxusijxiwjisx'''
from models.base import Base


class Rectangle(Base):
    '''hbduhehdueujdidjiweduddwdnwjn'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''hbhsuwhduw'''
        super().__init__(id)
        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''hdxbehdceudced'''
        return self.__width

    @width.setter
    def width(self, value):
        "hsjjxsjijxijs"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''hdbwjdiwjd'''
        return self.__height

    @height.setter
    def height(self, value):
        """hsjjzjjj"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''hdjjdhwidiwj'''
        return self.__x

    @x.setter
    def x(self, value):
        '''hsjkzkik'''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''hncxisjiciec'''
        return self.__y

    @y.setter
    def y(self, value):
        '''hxjhjkxioasox'''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''hsxkjsiaoxdskjijdf'''
        return self.width * self.height

    def display(self):
        '''hqhsuhsuhuhwsuhj'''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        '''hujeifnwekfiwfkjwofiwjk'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''hjshncujhschchlkc'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''hjdncjcjijdohjiuhfvhfv'''
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''hjcjjdchdhdcjijweif'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
