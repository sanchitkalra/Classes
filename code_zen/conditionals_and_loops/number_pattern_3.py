size = int(input())

print(1)
for k in range(1, size):
    print(1, end = "")
    for j in range(k-1):
        print(2, end = "")
    print(1, end = "")
    print("")