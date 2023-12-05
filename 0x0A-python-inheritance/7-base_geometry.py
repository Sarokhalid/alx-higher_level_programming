#!/usr/bin/python3
"""basegeometry class"""


class BaseGeometry:
    """ class BaseGeometry"""
    def area(self):
        """
        Calculate the area
        Raises:
            Exception: This method is not implemented
            in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate if the value is an integer and greater than 0
        Args:
            name (str): The name of the value.
            value: The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
