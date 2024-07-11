
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

# the docstring can be accessed through:

# 1) using the __doc__ method of the object.
print(my_square.__doc__)

# 2) using the help() function.
help(my_square)