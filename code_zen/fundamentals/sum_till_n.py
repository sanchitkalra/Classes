# find sum of numbers until N
# https://codezen.codingninjas.com/practice/8546/965/sum-of-even-numbers-till-n

limit = int(input())

sum = 0

for k in range(1, limit+1):
    if (k%2 == 0):
        sum += k

print(sum)