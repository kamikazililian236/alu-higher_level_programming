#!/usr/bin/python3
"""
This module provides a function to print a square of hash (#) characters.
"""


def print_square(size):
    """
    Prints a square of size length using #.
    size must be an integer >= 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
