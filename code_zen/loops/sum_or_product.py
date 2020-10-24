def product(number):
    result = 1
    for k in range(1, number+1):
        result *= k
    return result

def sum(number):
    sum = 0
    for k in range(1, number+1):
        sum += k
    return sum

number = int(input())
opr = int(input())

if opr == 1:
    print(sum(number))
elif opr == 2:
    print(product(number))
else:
    print(-1)