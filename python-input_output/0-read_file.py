#!/usr/bin/python3
"""
python program
"""


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to stdout.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
