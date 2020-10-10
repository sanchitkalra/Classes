#size = int(input())
size = 9
for k in range(size):
    for j in range(k+1, 0, -1):
        print(2**(j-1), end = " ")
    print("")