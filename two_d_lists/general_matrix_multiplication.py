arr1 = [[1, 7, 3],
        [3, 5, 6],
        [6, 8, 9]]

arr2 = [[1, 1, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]]

result = [ [0 for x in range(len(arr2[0]))] for x in range(len(arr1[0])) ]
print(result)

def element_result(arr1, arr2, x, y):
    x = 0
    for k in range(len(arr2[0])):
        for j in range(len(arr1[0])):
            x += arr1[x][j] * arr2[k][y]
    return x

element_result(arr1, arr2, 1, 0)
