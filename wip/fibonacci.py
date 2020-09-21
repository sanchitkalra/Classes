#Print all fibonacci numbers until N

x = 3
 
n = int(input())

f_sum = 2

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    while x <= (n-2):
        temp = x
        f_sum = f_sum + temp
        x = x + 1

print(f_sum)