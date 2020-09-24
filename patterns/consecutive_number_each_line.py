size = int(input())

i = 1
j = size

while i <= size:
    for k in range(1, j+1):
        print(k, end = "")
    print("")
    i += 1