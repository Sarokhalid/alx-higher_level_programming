#!/usr/bin/python3
"""fhkk"""
import sys
from typing import List


def save_to_json_file(my_obj, filename):
    """dhkk"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """dhkk"""
    with open(filename, "r") as file:
        return json.load(file)


def add_arguments_to_list(arguments: List[str]):
    """cdhkkl"""
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []
    existing_list.extend(arguments)
    save_to_json_file(existing_list, "add_item.json")


arguments = sys.argv[1:]
add_arguments_to_list(arguments)
