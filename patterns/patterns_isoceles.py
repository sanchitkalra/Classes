size = int(input())

i = 1

while i <= size:
    for k in range(1, size - i +1):
        print(" ", end = "")
    for k in range(1, i+1):
        print(k, end = "")
    for k in range(i-1, 0, -1):
        print(k, end = "")
    for k in range(1, size - i +1):
        print(" ", end = "")
    print("")
    i += 1