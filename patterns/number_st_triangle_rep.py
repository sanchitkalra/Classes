size = int(input())

i = 1
j = size

index = 1

while i <= size:
    for k in range(index, i+index):
        print(k, end = "")
        index += 1
    print("")
    i += 1

# simpler solution below

size = int(input())

i = 1
index = 1

while i <= size:
    j = 1
    while j <= i:
        print(index, end = "")
        index += 1
        j += 1
    print("")
    i += 1