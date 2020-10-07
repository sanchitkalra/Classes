# print a triangle pattern
# https://codezen.codingninjas.com/practice/463/654/give-me-triangle

size = int(input())

for k in range(size):
    print(" "*k, end = "")
    print("*"*(size-k), end = "")
    print("")