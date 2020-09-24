size = int(input())

i = 1
j = 1

while i <= size:
    while j <= size:
        for k in range(1, j+1):
            print("*", end= "")
        print("")
        j += 1
    i += 1