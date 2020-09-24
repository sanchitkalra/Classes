size = int(input())

i = 1
j = size

while i <= size:
    for k in range(j):
        print("*", end = " ")
    print("")
    i += 1