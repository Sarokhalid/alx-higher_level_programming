#!/usr/bin/python3
"""class vbn"""


class BaseGeometry:
    """jggjk"""
    def area(self):
        """
        Calculate the are
        Raises:
            Exception: This method is not implemented in the base class.
        """
    raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as a positive integer.
        Args:
            name (str): The name of the value.
            value: The value to be validated.
        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be a positive integer")


class Rectangle(BaseGeometry):
    """jjgfjk"""
    def __init__(self, width, height):
        """
        Initialize a Rectangle object with width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is not a positive integer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = heigh

    def area(self):
        """
        Calculate the area of the rectangle.
        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Get the string representation of the rectangle.
        Returns:
            str: The string representation of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """jhgfhhffh"""
    def __init__(self, size):
        """
        Initialize a Square object with size.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not a positive integer
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
