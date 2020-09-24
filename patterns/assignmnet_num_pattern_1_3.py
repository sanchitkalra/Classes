size = int(input())

i = 1

print("1")
while i <= size-1:
    print("1", end = "")
    for k in range(i-1):
        print("2", end = "")
    print("1")
    i += 1