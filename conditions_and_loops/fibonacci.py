limit = int(input())

a = 0
b = 1

i = 1

while i <= limit:
    c = a + b
    a = b
    b = c
    i += 1
    
print(a)