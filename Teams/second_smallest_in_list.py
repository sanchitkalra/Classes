# return the second smallest number in a list

arr = [1, 2, 1, 1, 1, 3, 4, 5, 6, 2, 8, 6, 4, 3, 2, 1, 1, 3, 4, 5, 6, 3, 4, 3, 3, 2, 4, 8]

def secondSmallest(arr):
    smallest = min(arr)
    smallest_n = arr.count(smallest)

    for k in range(smallest_n):
        arr.remove(smallest)

    second_smallest = min(arr)
    return second_smallest

print(secondSmallest(arr))