#!/usr/bin/python3

class BaseGeometry:
    """BaseGeometry class with area and integer validation methods"""
    
    def area(self):
        """Raises an exception indicating that the method is not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
