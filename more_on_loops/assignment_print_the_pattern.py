size = int(input())

# size = 5

# index = 1

# # for k in range(0, size, 2):
# #     for i in range(1, size+1):
# #         x = (k*size) + i
# #         print(x, " ", end = "")
# #     print("")

# for k in range(size-1, 0, -2):
#     for i in range(1, size+1):
#         x = (k*size) + i
#         print(x, " ", end = "")
#     print("")

# size = 4

startValue = 1

for i in range(1, size+1):
    for j in range(startValue, startValue + size):
        print(j, end = " ")
    print("")
    if (i == ((size+1)//2)):
        if (size%2) != 0:
            startValue = size*(size-2) + 1
        else:
            startValue = size*(size-1) + 1
    elif i > ((size+1)//2):
        startValue = startValue - 2*size
    else:
        startValue = startValue + 2*size