#!/usr/bin/python3
"""fghjj"""


class BaseGeometry:
    """class"""
    def area(self):
        """
        Calculate the area.
        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as a positive integer.
        Args:
            name (str): The name of the value
            alue: The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be a positive integer")


class Rectangle(BaseGeometry):
    """class base"""
    def __init__(self, width, height):
        """
        Initialize a Rectangle object with width and heigh
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Get the string representation of the rectangle.
        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
