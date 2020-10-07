# Print a binary pattern
# https://codezen.codingninjas.com/practice/463/662/binary-pattern

size = int(input())

for k in range(1, size+1):
    if k%2 == 0:
        for j in range(size - k + 1):
            print("0", end = "")
    else:
        for j in range(size - k + 1):
            print("1", end = "")
    print("")