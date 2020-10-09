# the following is the submitted solution and a tests are provided below

from sys import stdin

def swapAlternate(arr, n) :
    #Your code goes here
    length = len(arr)
    if length % 2 == 0:
        for k in range(0, length, 2):
            arr[k], arr[k+1] = arr[k+1], arr[k]
    else:
        for k in range(0, length - 1, 2):
            arr[k], arr[k+1] = arr[k+1], arr[k]

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#Printing the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    arr, n = takeInput()
    if n != 0 :
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1

# alternative solution

for k in range(0, len(arr)-1, 2):
    arr[k], arr[k+1] = arr[k+1], arr[k]

# ---------------------------------------------------------------------------------------------------------
# code used for testing algorithm, no need to use it
# the following are test cases tested independently for logical testing, you may refer to them for dry runs
# ---------------------------------------------------------------------------------------------------------

arr = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    [1, 2, 3, 4, 5, 6],
    [9, 3, 6, 12, 4, 32, 5, 11, 19]
]

for k in range(3):
    print("Array at " + str(k))
    x = arr[k]
    print(x)
    # if len(x) >= 10:
    #     for i in range(0, (len(x)//2) + 5, 2):
    #         x[i], x[i+1] = x[i+1], x[i]
    #         print("x at "+str(i)+"th is ", x)
    # else:
    #     for i in range(0, (len(x)//2) + 3, 2):
    #         x[i], x[i+1] = x[i+1], x[i]
    #         print("x at "+str(i)+"th is ", x)
    # print(x)
    if (len(x) % 2) == 0:
        for i in range(0, len(x), 2):
            x[i], x[i+1] = x[i+1], x[i]
            print("x at "+str(i)+"th is ", x)
    else:
        for i in range(0, len(x) - 1, 2):
            x[i], x[i+1] = x[i+1], x[i]
            print("x at "+str(i)+"th is ", x)
    print(x)
    print("--------")

# ---------------------------------
# IGNORE EVERYTHING BELOW THIS LINE
# ---------------------------------

# length = len(arr)
# print("arr1")
# print(arr)

# for k in range(0, (length//2) + 5, 2):
#     temp = arr[k]
#     arr[k] = arr[k+1]
#     arr[k+1] = temp
#     print("arr at ", k, "th is: ", arr)

# print(arr)

# print("")

# print("arr2")

# length2 = len(arr2)
# print(arr2)

# for k in range(0, (length//2), 2):
#     temp = arr2[k]
#     arr2[k] = arr2[k+1]
#     arr2[k+1] = temp
#     print("arr at ", k, "th is: ", arr2)

# print(arr2)

# print("")
# print("arr3")

# length2 = len(arr3)
# print(arr3)

# for k in range(0, (length//2), 2):
#     temp = arr3[k]
#     arr3[k] = arr3[k+1]
#     arr3[k+1] = temp
#     print("arr at ", k, "th is: ", arr3)

# print(arr3)
