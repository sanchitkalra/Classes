import take_input
import print_list

# input: size (row * columns) followed by elements of each row
#arr1 = take_input.takeInputM1()
#arr2 = take_input.takeInputM1()

arr1 = [[1, 2, 3], 
        [2, 3, 4],
        [1, 2, 5]
    ]
arr2 = [[3, 4, 5], 
        [5, 2, 1],
        [3, 1, 2]
    ]

result = [ [ 0 for x in range(len(arr1[0])) ] for x in range(len(arr1)) ]
result_x = [ [ 0 for x in range(len(arr1[0])) ] for x in range(len(arr1)) ]

for k in range(len(arr1)):
    for j in range(len(arr1[0])):
        result[k][j] = arr1[k][j] + arr2[k][j]

result_x = [ [arr1[x][y] + arr2[x][y] for y in range(len(arr1[0]))] for x in range(len(arr1)) ]

print("result w/ for loops")
print_list.printList4(result)
print("result w/ list comprehension")
print_list.printList4(result_x)