#!/usr/bin/python3
"""this is class BaseGeometry"""


class BaseGeometry:
    def area(self):
        """
        Calculate the area.
        Raises:
            Exception: This method is not implemented
            in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as an integer.
        Args:
            name (str): The name of the value.
            value: The value to be validated
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initialize a Rectangle object with width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not a positive integer.
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
