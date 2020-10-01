size = int(input())

i = 1

for i in range(1, size+1, 2):
    spaces = (size - i)//2
    print(" "*spaces, end = "")
    print("*"*i)

for j in range(size - 2, 0, -2):
    spaces = (size - j)//2
    print(" "*spaces, end = "")
    print("*"*j)