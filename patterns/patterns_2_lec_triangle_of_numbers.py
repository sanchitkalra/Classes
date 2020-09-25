size = int(input())

i = 1

# while i <= size:
#     for k in range(size-i):
#         print(" ", end = "")
#     for k in range(index+i, index+size-i):
#         print(k, end = "")
#     for k in range(index-i+1, 0, -1):
#         print(k, end = "")
#     for k in range(size-i):
#         print(k, end = "")
#     print("")
#     i += 1
#     index += 1

while i <= size:
    x = 0
    for k in range(size-i):
        print(" ", end = "")
    for k in range(i, (i*2)):
        print(k, end = "")
        x = k
    for k in range(x-1, i-1, -1):
        print(k, end = "")
    print("")
    i += 1