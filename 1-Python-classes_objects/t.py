class Square:
    """
    A class that defines a square.

    Attributes:
        size (int): size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property

    # getter
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be integer.")
        #elif value <= 0:
        #    raise ValueError("size must be greater than 0 and not negative.")
        self.__size = value
    def area(self):
        """
        This function returns the area of the new square.

        Returns:
            the area of the square.
        """
        return self.__size * self.__size
    
    
    @property

    def position(self):
        return self.__position
    
    @position.setter

    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(value, int) for num in value) or
                not all(num >= 0 for num in value)):
               raise TypeError("position must be a tuple of 2 positive integers")
        
        self.__position = value

    def my_print(self):
       # for row in range(0, self.__size):
        #    for col in range(self.__size):
         #print("#", end="")
         #   print("")
        if self.__size == 0:
            print("")
            return
        
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
