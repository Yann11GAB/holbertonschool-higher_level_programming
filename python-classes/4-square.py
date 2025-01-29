#!/usr/bin/python3
"""
Python program to define a Square class with getter and setter for size
"""


class Square:
    """
    A class that defines a square by its size
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance

        Args:
            size (int): The size of the square's side. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square

        Returns:
            int: The size of the square's side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        Args:
            value (int): The size of the square's side

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
