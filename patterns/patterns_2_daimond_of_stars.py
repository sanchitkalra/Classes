size = int(input())

i = 1

while i <= size:
    spaces = (size - i)//2
    print(" "*spaces, end = "")
    print("*"*i)
    i += 2

j = size - 2

while j >= 1:
    spaces = (size - j)//2
    print(" "*spaces, end = "")
    print("*"*j)
    j -= 2