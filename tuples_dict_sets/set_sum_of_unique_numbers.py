def sumUnique(arr):
    arr_set = set(arr)
    return sum(arr_set)

arr = [int(x) for x in input().split()]

print(sumUnique(arr))