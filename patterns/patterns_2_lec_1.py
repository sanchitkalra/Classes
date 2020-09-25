# print a pattern as follows 
# for n = 4:
# 4444
# 333
# 22
# 1

size = int(input())

i = size

while i >= 1:
    for k in range(1, i+1):
        print(i, end = "")
    print("")
    i -= 1