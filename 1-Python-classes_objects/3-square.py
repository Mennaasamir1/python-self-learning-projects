#!/usr/bin/python3

class Square:
    """
    A class that defines a square.

    Attributes:
        size (int): size of the square.
    """
    def __init__(self, size):
        """
        Initializes a new square object.

        Parameters:
            size (int): size of the new square.
        """
        self.__size = size

    @property

    # getter
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be integer.")
        elif value <= 0:
            raise ValueError("size must be greater than 0 and not negative.")
        self.__size = value
    def area(self):
        """
        This function returns the area of the new square.

        Returns:
            the area of the square.
        """
        return self.__size * self.__size