#size = int(input())

size = 5

i = 1

while i <= size:
    x = 0
    for k in range(size-i):
        print(" ", end = "")
    for k in range(1, i+1):
        print("*", end = "")
        x = k
    # for k in range(x-1):
    #     print("*", end = "")
    print("")
    i += 1