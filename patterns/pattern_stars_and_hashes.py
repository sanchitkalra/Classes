size = int(input())

for k in range(size):
    for j in range(size - k - 1):
        print(" ", end = "")
    for j in range(k):
        print("#", end = "")
    print("*", end = "")
    for j in range(k):
        print("#", end = "")
    print("")