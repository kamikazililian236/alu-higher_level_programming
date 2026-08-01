#!/usr/bin/python3
"""
This module provides a function to format text with newlines.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of: ., ? and :
    Strips leading and trailing spaces on each formatted line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    # Skip leading spaces of the initial text
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            # Skip subsequent spaces after special characters
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
