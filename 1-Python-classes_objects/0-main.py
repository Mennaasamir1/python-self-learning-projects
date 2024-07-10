#!/usr/bin/python3

Person = __import__('0-older').Person

p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)

p1.CalcAge()
p2.CalcAge()
p3.CalcAge()