size = int(input())

print(1)
for k in range(1, size):
    print(k, end = "")
    for j in range(k-1):
        print(0, end = "")
    print(k, end = "")
    print("")