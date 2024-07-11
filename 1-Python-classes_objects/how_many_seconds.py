#!/usr/bin/python3

class Age:
    def __init__(self, age):
        self.age = age

    def convert_into_days(self):
        result = 0
        for i in range(self.age):
            i *= 365
            result += i
        return result
    
person = Age(24)

print(f"hey, you've lived for: {person.convert_into_days()}")

