arr = [0, 1, 1, 0, 1, 0, 1]
arr = [1, 0, 1, 1, 0, 1, 0, 1]
#arr = [0, 1, 0, 1, 0]

for k in range(len(arr)):
    if arr[k] == 0:
        arr.pop(k)
        arr.insert(0, 0)
    else:
        arr.pop(k)
        arr.append(1)

for k in range(len(arr)):
    if arr[k] == 0:
        arr.pop(k)
        arr.insert(0, 0)
    else:
        arr.pop(k)
        arr.append(1)

print(arr)