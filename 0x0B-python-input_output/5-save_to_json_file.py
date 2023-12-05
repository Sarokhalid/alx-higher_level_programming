#!/usr/bin/python3
"""fhjk"""
import json


def save_to_json_file(my_obj, filename):
    """fhjkk"""
    with open(filename, mode='w') as file:
        json.dump(my_obj, file)
