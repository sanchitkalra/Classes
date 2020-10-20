# print sum of column with largest sum

arr = [
    [1, 2, 3, 4],
    [8, 7, 6, 5],
    [13, 14, 15, 16]
]

sum_arr = []

for k in range(len(arr[0])):
    sum = 0
    for j in range(len(arr)):
        sum += arr[j][k]
    sum_arr.append(sum)

print(max(sum_arr))