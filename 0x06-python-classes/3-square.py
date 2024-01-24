#!/usr/bin/python3
"""
Module - 3-square
Defines a class Square with a private instance attribute size
and a public instance method area.
"""


class Square:
    """
    Square class with a private instance attribute size
    and a public instance method area.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2
