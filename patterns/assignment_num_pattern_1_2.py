size = int(input())

i = 1

print("1")
while i <= size-1:
    print(i, end = "")
    for k in range(i-1):
        print("0", end = "")
    print(i)
    i += 1