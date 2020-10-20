# calculate the transpose for a 3x3 matrix

transpose = [ [0 for x in range(3)] for k in range(3) ]
print(transpose)

arr =  [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def transposer(arr, transpose):
    for k in range(len(arr)):
        for j in range(len(arr[0])):
            transpose[j][k] = arr[k][j]

transposer(arr, transpose)
for k in range(len(transpose)):
    print(transpose[k])