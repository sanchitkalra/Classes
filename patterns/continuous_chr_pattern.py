# https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/amp/

size = int(input())

index = ord("A")

for k in range(size):
    for j in range(index, index+k+1):
        print(chr(j), end = " ")
    print("")
    index += k+1