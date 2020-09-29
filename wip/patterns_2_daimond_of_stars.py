#size = int(input())
size = 5

i = 1

while i <= size:
    x = (i//2) + 1
    for k in range(x+1):
        print(" ", end = "")
    for k in range(size-x):
        print("*", end = "")
    print("")
    i += 1