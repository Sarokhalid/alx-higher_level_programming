!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """
    Rectangle class defines a rectangle shape.
    Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.
        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width attribute.
        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.
        Args:
            value (int): The width value to set.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.
        Args:
            value (int): The height value to set.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        Returns:
            str: The string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        Returns:
            str: The string representation of the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
