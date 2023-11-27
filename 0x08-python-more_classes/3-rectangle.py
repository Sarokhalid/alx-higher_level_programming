#!/usr/bin/python3
"""ghdhqjdjdkej"""


class Rectangle:
    """hbxhsbhcgvghs"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
     def width(self):
     """jljfiwhufvhwuvhuw"""
         return self.__width
	
    @width.setter
    def width(self, value):
        """knckancjadncjnc"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """kjncakcnjancjanjnvjanvcjn"""
        return self.__height

    @height.setter
    def height(self, value):
        """jncajcnjadcnjdndjjvcdn"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """jcndajcjancjnvjcnj"""
        return self.width * self.height

    def perimeter(self):
        """hwhefhwefehbkwhfkwjfh"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """jnxcjdacdabchadb"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = "#" * self.width + "\n"
        rectangle *= self.height - 1
        rectangle += "#" * self.width
        return rectangle
