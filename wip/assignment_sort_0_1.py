arr = [0, 1, 1, 0, 1, 0, 1]

for k in range(len(arr)):
    if arr[k] == 0:
        arr[k], arr[0] = arr[0], arr[k]
    else:
        arr[k], arr[-1] = arr[-1], arr[k]

print(arr)