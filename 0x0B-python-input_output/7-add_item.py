#!/usr/bin/python3
"""fhjjj"""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

try:
    existing_data = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_data = []
arguments = sys.argv[1:]
data = existing_data + arguments
save_to_json_file(data, "add_item.json")
