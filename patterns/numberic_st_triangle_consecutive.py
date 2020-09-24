size = int(input())

i = 1
j = size

x = 1

while i <= size:
    for k in range(i):
        print(x, end = "")
        x += 1
    print("")
    i += 1