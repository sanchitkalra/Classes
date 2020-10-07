size = int(input())

print("1"*size)

for k in range(size - 2):
    print("1", end = "")
    for j in range(size - 2):
        print(" ", end = "")
    print(str(size))

print(str(size)*size)