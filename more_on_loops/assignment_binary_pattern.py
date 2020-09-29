size = int(input())

for k in range(size):
    if k%2 == 0:
        for j in range(size-k):
            print("1", end = "")
    else:
        for j in range(size-k):
            print("0", end = "")
    print("")