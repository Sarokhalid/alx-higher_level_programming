#!/usr/bin/python3
"""gjjkk"""
import json


def load_from_json_file(filename):
    """dhjk"""
    with open(filename, mode='r') as file:
        return json.load(file)
