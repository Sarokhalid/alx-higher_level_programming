#!/usr/bin/python3
"""
define rectangle
"""


class Rectangle:
    """class rapresantation rectangle"""
    def __init__(self, width=0, height=0):
        """intialization rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """height of rerctangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an intege")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of reactangle"""
        return self.width * self.height

    def perimeter(self):
        """perimeter of rectangle"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """jnxcjdacdabchadb"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = "#" * self.width + "\n"
        rectangle *= self.height - 1
        rectangle += "#" * self.width
        return rectangle
