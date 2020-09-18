#largest number

a = int(input("first number: "))
b = int(input("second number: "))
c = int(input("third number: "))

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)