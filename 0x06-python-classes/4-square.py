#!/usr/bin/python3
""" square module """


class Square:
    """ class square """
    def __init__(self, size=0):
        """
        initilazation
        Args:
        size: length
        """
        self.__size = size

    @property
    def size(self):
        """
        Raises and property
        """
        return self.__size

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError('size must be an integere')
            if value < 0:
                raise ValueError('size must be >= 0')
            self.__size = value
