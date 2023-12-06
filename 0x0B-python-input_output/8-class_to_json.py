#!/usr/bin/python3
"""fhjk"""


def class_to_json(obj):
    """fhjk"""
    json_dict = {}
    attributes = obj.__dict__
    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
