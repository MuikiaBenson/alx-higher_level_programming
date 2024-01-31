#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Args:
        first_name(str): The first name.
        last_name(str, optional): The last name.

    Raises:
        TypeError: If first_name or last_name is not a string.

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = "My name is {} {}".format(first_name, last_name)
    print(full_name)
