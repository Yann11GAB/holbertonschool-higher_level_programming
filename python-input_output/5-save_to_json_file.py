#!/usr/bin/python3
"""
python program
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation.
    """
    with open(filename, "w", encoding="UTF-8") as file:
        json.dump(my_obj, file)
