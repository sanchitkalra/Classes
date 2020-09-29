size = int(input())

i = 1

while i <= size:
    for k in range(1, size+1):
        if k == i:
            print("*", end = "")
        else:
            print("0", end = "")
    print("*", end = "")
    for k in range(size, 0, -1):
        if k == i:
            print("*", end = "")
        else:
            print("0", end = "")
    print("")
    i += 1