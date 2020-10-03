# from sys import stdin

# def swapAlternate(arr, n) :
#     #Your code goes here
#     length = len(arr)
#     for k in range(0, (length//2)+2, 2):
#         temp = arr[k]
#         arr[k] = arr[k+1]
#         arr[k+1] = temp

# #Taking Input Using Fast I/O
# def takeInput() :
#     n = int(stdin.readline().rstrip())

#     if n == 0 :
#         return list(), 0

#     arr = list(map(int, stdin.readline().rstrip().split(" ")))
#     return arr, n


# #Printing the array/list
# def printList(arr, n) :
#     for i in range(n) :
#         print(arr[i], end = " ")
#     print()


# #main
# t = int(stdin.readline().rstrip())

# while t > 0 :
#     arr, n = takeInput()
#     if n != 0 :
#         swapAlternate(arr, n)
#         printList(arr, n)
#     t -= 1


# code used for testing algorithm, no need to use it

size = 6
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

arr2 = [1, 2, 3, 4, 5, 6]

length = len(arr)
print("arr1")
print(arr)

for k in range(0, (length//2), 2):
    temp = arr[k]
    arr[k] = arr[k+1]
    arr[k+1] = temp
    print("arr at ", k, "th is: ", arr)

print(arr)

print("")

print("arr2")

length2 = len(arr2)
print(arr2)

for k in range(0, (length//2), 2):
    temp = arr2[k]
    arr2[k] = arr2[k+1]
    arr2[k+1] = temp
    print("arr at ", k, "th is: ", arr2)

print(arr2)

