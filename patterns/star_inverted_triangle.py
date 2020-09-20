i = 1
j = 5

while i <= 5:
    while j >= 1:
        for k in range(1, j+1):
            print("*", end=" ")
        print("")
        j -= 1
    i += 1