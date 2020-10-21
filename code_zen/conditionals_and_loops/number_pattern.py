size = int(input())

for k in range(size):
    for j in range(1, size-k+1):
        print(j, end = "")
    print("")