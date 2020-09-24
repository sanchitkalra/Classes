size = int(input())

i = 1

while i <= size:
    index = ord("A")
    for k in range(index, index+size):
        print(chr(k), end = "")
    print("")
    i += 1