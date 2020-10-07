from sys import stdin

def sortZeroesAndOne(arr, n):
    zeros = 0
    for k in arr:
        if k == 0:
            zeros += 1
    for k in range(zeros):
        arr[k] = 0
    for k in range(zeros, n):
        arr[k] = 1

    # arr0 = []
    # arr1 = []
    # for k in arr:
    #     if k == 0:
    #         arr0.append(0)
    #     else:
    #         arr1.append(1)
    # print(arr0 + arr1)
    # return arr0 + arr1

    # # for k in range(len(arr)+1):
    # #     for k in range(len(arr)):
    # #         if arr[k] == 0:
    # #             arr.pop(k)
    # #             arr.insert(0, 0)
    # #         else:
    # #             arr.pop(k)
    # #             arr.append(1)
    
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()

    t -= 1





# arr = [0, 1, 1, 0, 1, 0, 1]
# arr = [1, 0, 1, 1, 0, 1, 0, 1]
# #arr = [0, 1, 0, 1, 0]
# arr = [1, 1, 0, 0, 1, 0]

# itr = 0

# arr0 = []
# arr1 = []

# for k in arr:
#     if k == 0:
#         arr0.append(0)
#     else:
#         arr1.append(1)
# arr = arr0 + arr1
# print(arr)
# print("---- ------ ------")

# # for k in range(len(arr)):
# #     if arr[k] == 0:
# #         arr.pop(k)
# #         arr.insert(0, 0)
# #         print("arr at {}th itr is: {}".format(itr, arr))
# #         itr += 1
# #     else:
# #         arr.pop(k)
# #         arr.append(1)
# #         print("arr at {}th itr is: {}".format(itr, arr))
# #         itr += 1

# # for k in range(len(arr)):
# #     if arr[k] == 0:
# #         arr.pop(k)
# #         arr.insert(0, 0)
# #         print("arr at {}th itr is: {}".format(itr, arr))
# #         itr += 1
# #     else:
# #         arr.pop(k)
# #         arr.append(1)
# #         print("arr at {}th itr is: {}".format(itr, arr))
# #         itr += 1

# for k in range(len(arr)+1):
#     for k in range(len(arr)):
#         if arr[k] == 0:
#             arr.pop(k)
#             arr.insert(0, 0)
#             print("arr at {}th itr is: {}".format(itr, arr))
#             itr += 1
#         else:
#             arr.pop(k)
#             arr.append(1)
#             print("arr at {}th itr is: {}".format(itr, arr))
#             itr += 1

# def sortZeroesAndOne(arr, n):
#     for k in range(len(arr)+1):
#         for k in range(len(arr)):
#             if arr[k] == 0:
#                 arr.pop(k)
#                 arr.insert(0, 0)
#             else:
#                 arr.pop(k)
#                 arr.append(1)
#     for k in arr:
#         print(k, end = " ")

# print("=-------------=")

# sortZeroesAndOne(arr, len(arr))
# print(arr)