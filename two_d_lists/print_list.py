arr = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
jagged = [ [1, 2, 3, 5], [2, 3, 5], [6, 7, 7, 3, 1, 1] ]

# method 1
# print all elements space seperated
def printList1(arr):
    for k in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[k][j], end = " ")
        print("")

printList1(arr)

# method 2
# prints any list, including jagged lists
def printList2(arr):
    for k in range(len(arr)):
        for j in range(len(arr[k])):
            print(arr[k][j], end = " ")
        print("")

printList2(jagged)

# method 3
# a better implementation for method 2
def printList3(arr):
    for row in arr:
        for element in row:
            print(element, end = " ")
        print("")

printList3(jagged)

# method 4
# using the join function
def printList4(arr):
    for row in arr:
        out = " ".join( [ str(element) for element in row ] )
        print(out)

printList4(jagged)