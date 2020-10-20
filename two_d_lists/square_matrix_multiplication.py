# perform nxn matrix multiplication

# performs actual multiplication and returns the result for the given input location
# arr1 is the first array and arr2 is the second array and x, y represent the position of the result required
def element_result(arr1, arr2, x, y):
    result = 0
    for k in range(len(arr1[x])):
        result += arr1[x][k] * arr2[k][y]
        # print(arr1[x][k])
        # print(arr2[k][y])
        # print(result)
        # print("")
    return result

# performs calculations for all elements in matrix
def multiply(arr1, arr2, result):
    for k in range(len(arr1)):
        for j in range(len(arr2)):
            result[k][j] = element_result(arr1, arr2, k, j)

    return result

# helper function to print the matrix in an easily readable format
def printMatrix(arr):
    for k in range(len(arr)):
        print(arr[k])

arr1 = [[1, 7, 3],
        [3, 5, 6],
        [6, 8, 9]]

arr2 = [
    [1, 2, 4],
    [3, 6, 12],
    [-2, -4, -8]
]

# arr1 = [
#     [1, 2],
#     [3, 4]
# ]

# arr2 = [
#     [5, 6],
#     [7, 8]
# ]

result = [ [ 0 for x in range(len(arr1)) ] for x in range(len(arr2)) ]

printMatrix(multiply(arr1, arr2, result))