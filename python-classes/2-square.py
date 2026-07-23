#!/usr/bin/python3
"""
This module defines a class Square with optional size and type/value validation.
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

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
