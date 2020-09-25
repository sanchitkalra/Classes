# print characters in reverse in terms of ordiality

size  = int(input())

# n = 5
# i = 1

# while i <= n:
#     j = 1
#     sc = chr(ord("A")+n-1)
#     while j <= i:
#         char = chr(ord(sc)-i+j)
#         print(char, end = "")
#         j += 1
#     print("")
#     i += 1

#size = 5
i = 1

while i <= size:
    j = 1
    index = chr(ord("A")+(size-1))
    while j <= i:
        x = chr(ord(index)-i+j)
        print(x, end = "")
        j += 1
    print("")
    i += 1

# size = 5

# i = 1
# ix = size - i 
# index = ord("A")

# while i <= size:
#     j = 1
#     while j <= i:
#         print(chr(index+ix-j+1), end = "")
#         j += 1
#     print("")
#     i += 1

# i = 1
# index = ord("A")

# while i <= size:
#     for k in range(size+index, i+index, -1):
#         print(chr(k), end = "")
#     print("")
#     i += 1

# i = 1

# while i <= size:
#     index = ord("A")
#     j = index + size - i
#     while j >= index:
#         print(chr(j), end = "")
#         j -= 1
#     print("")
#     i += 1
