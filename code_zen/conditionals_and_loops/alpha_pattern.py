size = int(input())

index = ord("A")
for k in range(size):
    character = index+k
    for j in range(k+1):
        print(chr(character), end = "")
    print("")