#!/usr/bin/python3
"""
Module defining the Student class
"""

class Student:
    """
    Class representing a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance
        """
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
