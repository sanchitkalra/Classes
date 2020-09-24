size = int(input())

i = 1
index = ord("A")

while i <= size:
    char = chr(index+i-1)
    for k in range(i):
        print(char, end = "")
    print("")
    i += 1