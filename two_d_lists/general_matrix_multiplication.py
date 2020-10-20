import print_list

arr1 = [[1, 7, 3],
        [3, 5, 6],
        [6, 8, 9]]

arr2 = [[1, 1, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]]

result = [ [0 for x in range(len(arr2[0]))] for x in range(len(arr1)) ]
#print(result)

def element_result(arr1, arr2, x, y):
    x = 0
    for k in range(len(arr2[0])):
        for j in range(len(arr1[0])):
            x += arr1[x][j] * arr2[k][y]
    return x

# element_result(arr1, arr2, 1, 0)

def multiply(arr1, arr2, result):
        rows = len(arr1)
        columns = len(arr2)
        j_cols = len(arr2[0])
        i = 0
        j = 0
        for i in range(rows):
                for j in range(j_cols):
                        for k in range(columns):
                                result[i][j] += arr1[i][k] * arr2[k][j]

multiply(arr1, arr2, result)
print_list.printList4(result)