size = int(input())

i = 1

while i <= size:
    for k in range(size-i):
        print(" ", end = "")
    for k in range(i, 0, -1):
        print(k, end = "")
    for k in range(2, i+1):
        print(k, end = "")
    print("")
    i += 1