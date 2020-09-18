#Number Reversal

#without a temp variable

a = int(input("number 1: "))
b = int(input("number 2: "))

a,b=b,a

print(a)
print(b)

#with a temp variable

c = int(input("number 1: "))
d = int(input("number 2: "))

temp = c
c = d
d = temp

print(c)
print(d)