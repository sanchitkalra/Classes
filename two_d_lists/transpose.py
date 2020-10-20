import print_list

# calculate the transpose for a n x m matrix

# arr =  [
#     [1, 2, 3],
#     [4, 5, 6],
#     [9, 10, 11]
# ]

arr =  [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = [ [0 for x in range(len(arr))] for k in range(len(arr[0])) ]
# transpose_x = [ [0 for x in range(len(arr[0])] for k in range(len(arr)) ]
#print(transpose)

def transposer(arr, transpose):
    for k in range(len(arr)):
        for j in range(len(arr[0])):
            transpose[j][k] = arr[k][j]

transposer(arr, transpose)
# for k in range(len(transpose)):
#     print(transpose[k])

# def transposerWithComprehension(arr, transpose_x):
#     transpose_x = [ [ arr[j][k] for j in range(len(arr[0])) ] for k in range(len(arr)) ]

print("transpose w/ for loops")
print_list.printList4(transpose)
# print("transpose w/ list comprehension")
# print_list.printList4(transpose_x)