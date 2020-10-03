size = int(input())

array = [int(x) for x in input().split()]

sum = 0

for k in array:
    sum += k

print(sum)