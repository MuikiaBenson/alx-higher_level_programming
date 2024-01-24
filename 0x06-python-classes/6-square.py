#!/usr/bin/python3
"""
Module - 6-square:
Defines a Square class with private size, position,
properties, and public methods.
"""


class Square:
    """
    Square class with private size, position, properties to retrieve
    and set size and position, and public methods area and my_print.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int, optional): The size of the square. Defaults to 0.
        - position (tuple, optional):Position of the square.Defaults to (0, 0)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes and returns the area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
