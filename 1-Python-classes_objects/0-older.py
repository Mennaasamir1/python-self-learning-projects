#!/usr/bin/python3
''' Compares another person's age to mine'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def CalcAge(self):
        if self.age > 24:
            print(f"{self.name} is older than me.")
        elif self.age == 24:
            print(f"{self.name} is the same age as me.")
        else:
            print(f"{self.name} is younger than me.")

#p1 = Person("Samuel", 24)
#p2 = Person("Joel", 36)
#p3 = Person("Lily", 24)

#p1.CalcAge()
#p2.CalcAge()
#p3.CalcAge()