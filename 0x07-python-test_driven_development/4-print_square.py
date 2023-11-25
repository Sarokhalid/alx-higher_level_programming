#!/usr/bin/python3
"""module for print_square methoed"""


def print_square(size):
    """methoed for printing a square with # characters
    Args:
       size: the int size of the square's side
    Raises:
       TypeError: if size is not an int
       ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print((("#" * size + "\n") * size), end"")


if __name__ == "__main__":
    import doctest
    doctest.textfile("tests/4-print_square.txt")
