#!/usr/bin/python3
"""this is module to check instancse"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance
    of the specified class.
    Args:
        obj: The object to be checked
        a_class: The class to compare
    Returns:
        True if the object is exactly an instance
        of the specified class, False otherwise.
   """
    return obj.__class__ is a_class
