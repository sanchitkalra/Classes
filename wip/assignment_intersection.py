# #  
# # Attempt 2
# # 

# import sys

# def intersections(arr1, n, arr2, m) :
#     intersection = [ list(set(arr1) and set(arr2)) ]
#     x = ""
#     for k in intersection:
#         x += str(k)
#     return x

# #Taking Input Using Fast I/O
# def takeInput() :
#     n = int(sys.stdin.readline().strip())
#     if n == 0:
#         return list(), 0

#     arr = list(map(int, sys.stdin.readline().strip().split(" ")))
#     return arr, n


# #main
# t = int(sys.stdin.readline().strip())

# while t > 0 :
#     arr1, n = takeInput()
#     arr2, m = takeInput()

#     intersections(arr1, n, arr2, m)
#     print()

#     t -= 1

# #  
# # Attempt 1
# # 

# # import sys

# # def intersections(arr1, n, arr2, m) :
# #     intersection = [ value for value in arr1 if value in arr2 ]
# #     x = ""
# #     for k in intersection:
# #         x += str(k)
# #     return x

# # #Taking Input Using Fast I/O
# # def takeInput() :
# #     n = int(sys.stdin.readline().strip())
# #     if n == 0:
# #         return list(), 0

# #     arr = list(map(int, sys.stdin.readline().strip().split(" ")))
# #     return arr, n


# # #main
# # t = int(sys.stdin.readline().strip())

# # while t > 0 :
# #     arr1, n = takeInput()
# #     arr2, m = takeInput()

# #     intersections(arr1, n, arr2, m)
# #     print()

# #     t -= 1

#---------------------------------------------------
# logical testing
#---------------------------------------------------

arr = [
    [6, 9, 8, 5],
    [9, 2, 4, 1, 8]
]

# arr = [
#     [2, 6, 1, 2],
#     [1, 2, 3, 4, 2]
# ]

temp1 = []
temp2 = []

intersection = []

for k in arr[0]:
    for j in arr[1]:
        if k == j:
            arr[1].remove(j)
            intersection.append(j)


print(intersection)

#-------------------------------------------------------------------------
# everything below this line are experiments, some do not work as intended
#-------------------------------------------------------------------------

# for k in range(len(arr[1])):
#     for j in arr[0]:
#         try:
#             if arr[1][k] == j:
#                 print("curr itr: k = {} and j = {}".format(k, j))
#                 print("arr before operations")
#                 print(arr[1])
#                 print(arr[0])
#                 intersection.append(j)
#                 arr[1].remove(j)
#                 arr[0].remove(j)
#                 print("arr after operations")
#                 print(arr[1])
#                 print(arr[0])
#                 print("-----------------------")
#                 print("intersection is")
#                 print(intersection)
#                 print("")
#         except:
#             print("index error occured")


# if len(arr[0]) <= len(arr[1]:
#     for i in range(len(arr[0])):
#         for k in arr[1]:
#             if k == arr[0][i]:
#                 arr[0].remove(k)
#                 arr[1].remove(k)
#                 print(arr[0])
#                 print(arr[1])
#                 intersection.append(k)
# else:
#     for i in range(len(arr[1])):
#         for k in arr[0]:
#             if k == arr[1][i]:
#                 intersection.append(k)

# for i in range(len(arr[0])):
#     for k in arr[1]:
#         if k == arr[0][i]:
#             intersection.append(k)

# print(intersection)