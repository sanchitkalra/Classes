arr = [1, 5, 3, 7, 2, 6, 0]

# solution using a combination of while and for loops

i = 0
while i <= (len(arr)-2):
    smallest = arr[i]
    index = -1
    for k in range(i, len(arr)):
        if arr[k] <= smallest:
            smallest = arr[k]
            index = k
    arr[i], arr[index] = arr[index], arr[i]
    print("arr at {}th iteration is {}".format(i, arr))
    i += 1

print(arr)

# from random import randint

# arr = [randint(-500, 500) for x in range(10000)]

# i = 0
# while i <= (len(arr)-2):
#     smallest = arr[i]
#     index = -1
#     for k in range(i, len(arr)):
#         if arr[k] <= smallest:
#             smallest = arr[k]
#             index = k
#     arr[i], arr[index] = arr[index], arr[i]
#     print("arr at {}th iteration is {}".format(i, arr))
#     i += 1

# print(arr)

# solution using only for loops 
arr = [1, 5, 3, 7, 2, 6, 0]

for i in range(len(arr)-1):
    smallest = arr[i]
    index = -1
    for k in range(i, len(arr)):
        if arr[k] <= smallest:
            smallest = arr[k]
            index = k
    arr[index], arr[i] = arr[i], arr[index]
    print("arr at {}th iteration is {}".format(i, arr))

print(arr)

# # solution using only while loops
# to be implemented