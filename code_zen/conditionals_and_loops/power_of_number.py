data = [int(x) for x in input().split()]

number = data[0]
power = data[1]
result = 1

for k in range(power):
    result *= number

print(result)