#!/usr/bin/python3
"""
This module defines a class Square with getter and setter properties for size.
"""


class Square:
    """
    Class Square that defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes the Square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
