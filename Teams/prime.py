#check if a number is a prime 

a = int(input())

i = 2
limit = (a//2)+1

prime = False

while i<=limit:
    if a%i !=0:
        i+=1
        prime = True
    else:
        prime = False
        break

if prime:
    print("prime")
else:
    print("not prime")