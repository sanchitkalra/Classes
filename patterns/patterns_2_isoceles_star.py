size = int(input())

i = 1

while i <= size:
    for k in range(size-i):
        print(" ", end = "")
    for k in range(i):
        print("*", end = "")
    for k in range(i-1):
        print("*", end = "")
    for k in range(size-i):
        print(" ", end = "")
    print("")
    i += 1