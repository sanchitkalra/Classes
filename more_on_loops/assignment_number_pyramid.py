size = int(input())

for k in range(1, size):
    flag = False
    x = 0
    for j in range(k-1, 0, -1):
        if j == size-1:
            continue
        print(" ", end = "")
    for j in range(k, size+1):
        if j == k == size:
            flag = True
            continue
        print(j, end = "")
        x = j
    if not flag:
        print("")

    # if flag:
    #     continue
    # else:
    #     print("")

for k in range(size):
    for j in range(size-k, 1, -1):
        print(" ", end = "")
    for j in range(size-k, size+1):
        print(j, end = "")
    print("")