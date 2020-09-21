i = 1
j = 1

while i <= 5:
    while j <= 5:
        for k in range(1, j+1):
            print(j, end = " ")
        print("")
        j += 1
    i += 1