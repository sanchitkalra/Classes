size = 5

for k in range(size):
    for j in range(size, k, -1):
        print(j, end = " ")
    for j in range(k):
        print(" ", end = " ")
    for j in range(k):
        print(" ", end = " ")
    for j in range(k+1, size+1):
        print(j, end = " ")
    print("")