size = int(input())

i = 1
j = size

while i <= size:
    for k in range(i, 0, -1):
        print(k, end = "")
    print("")
    i += 1