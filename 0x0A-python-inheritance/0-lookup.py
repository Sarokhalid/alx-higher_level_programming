#!/usr/bin/python3
"""retrive attribute and methoeds"""


def lookup(obj):
    """retrive metheo and attributes
    Args:
        obj: object
    Returns:
        retrive attribute and methoeds
    """
    return [attr for attr in dir(obj) if not attr.startswith('__')]
