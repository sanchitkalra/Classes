arr = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

rows = len(arr)
columns = len(arr[0])

def checkIdentity(arr):
    flag = True
    rows = len(arr)
    columns = len(arr[0])
    for k in range(rows):
        for j in range(columns):
            if not (k == j and arr[k][j] == 1) or (k != j and arr[k][j] == 0):
                flag = False
            else:
                flag = True

    return flag

print(checkIdentity(arr))

#flag = False

# for k in range(rows):
#     for j in range(columns):
#         if (k == j and arr[k][j] == 1) or (k!=j and arr[k][j] == 0):
#             flag = True
#         else:
#             flag = False
#             break
#     if flag == False:
#         break

#print(flag)