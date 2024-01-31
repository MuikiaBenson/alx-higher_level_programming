#!/usr/bin/python3
"""Defines a function that adds two integer functions"""


def add_integer(a, b=98):
    """
    Args:
        a (int or float): First number.
        b (int or float): Second number with 98 set as default.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
