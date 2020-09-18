#Solve Quadratic Equation

import cmath

print("enter quadratic equation in the format ax^2 + bx + c = 0")

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

d = b**2 - 4*a*c

print(d)


r1 = (-b + cmath.sqrt(d))/2
r2 = (-b - cmath.sqrt(d))/2
print(r1)
print(r2)
