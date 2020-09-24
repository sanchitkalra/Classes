size = int(input())

i = 1
index = ord("A")

while i <= size:
    for k in range(index, index+i):
        print(chr(k), end = "")
    print("")
    index += 1
    i += 1