#Sum of first n even numbers

a = int(input())

i = 1
sum = 0

while i<=a:
    if i%2 == 0:
        sum = sum + i
    i+=1
    
print(sum)