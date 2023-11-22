#!/usr/bin/python3
"""square module"""


class Square:
    """ reprecent square"""

    def __init__(self, size=0):
        """
        intialize a new square
        Args:
        size(int): thevsize of new square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
