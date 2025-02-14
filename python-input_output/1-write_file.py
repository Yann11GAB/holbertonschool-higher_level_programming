#!/usr/bin/python3
"""
python program
"""


def write_file(filename="", text=""):
    """
    Reads a UTF-8 encoded text file and prints its content to stdout.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return(file.write(text))
