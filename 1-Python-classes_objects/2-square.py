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

    def area(self):
        """
        This function returns the area of the new square.

        Returns:
            the area of the square.
        """
        return self.__size * self.__size