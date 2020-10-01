#size = int(input())

size = 5

# for k in range(x):
#     for j in range(x, -1, -1):
#         print(" ", end = "")
#     for n in range(1, x):
#         print("*", end = "")
#     print("")

# for k in range(size):
#     x = (size//2)+1
#     for j in range(x-1):
#         print(" "*j, end = "")
#     for n in range(1, size, 2):
#         print("*"*n, end = "")
#     print("")

for k in range(1, 4):
    for j in range(1, k+1):
        print("*", end = "")
    print("")