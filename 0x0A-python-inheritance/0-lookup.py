#!/usr/bin/python3
"""jgff"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object
    Args:
        obj: The object to lookup
    Returns:
        A list object containing the availabl
        attributes and methods
    """
    return dir(obj)
