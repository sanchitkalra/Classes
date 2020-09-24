size = int(input())

i = 1
index = ord("A")

while i <= size:
    for k in range(index, index+size):
        print(chr(k), end = "")
    print("")
    i += 1
    index += 1