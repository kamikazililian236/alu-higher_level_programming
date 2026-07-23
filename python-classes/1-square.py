#!/usr/bin/python3
"""
This module defines a class Square with a private size attribute.
"""


class Square:
    """
    Class Square that defines a square.
    """

    def __init__(self, size):
        """
        Initializes the Square with a size.

        Args:
            size: The size of the square.
        """
        self.__size = size
