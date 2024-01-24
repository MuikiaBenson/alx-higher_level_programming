#!/usr/bin/python3
"""
Module - 4-square
Defines a Square class with a private attribute size and a public method area.
"""


class Square:
    """
    Square class with a private attribute size,
    a getter property to retrieve it, and a setter property to set it.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes and returns the area."""
        return self.__size ** 2
