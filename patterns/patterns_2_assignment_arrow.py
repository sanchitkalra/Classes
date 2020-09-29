#size = int(input())
size = 11
i = 1

while i <= size:
    x = (i//2) + 1
    y = (i//2) + 2
    for k in range(2, y):
        print(" ", end = "")
    for k in range(x):
        print("* ", end = "")
    print("")
    i += 2

i = size

while i >= 2:
    x = (i//2) + 1
    y = (i//2) + 2
    for k in range(y-1, 2, -1):
        print(" ", end = "")
    for k in range(x-1, 0, -1):
        print("* ", end = "")
    print("")
    i -= 2