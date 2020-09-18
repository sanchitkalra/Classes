#Print all primes from 3 until N

N = int(input())

k = 1

#array to store all prime
all_primes = []

#loop from k to N, except 1
while k<=N:
    limit = (k//2)+1
    print("imit at k ", k, " is ", limit)
    i = 2
    
    prime = False

    #check prime condition for all k
    while i<=limit:
        if k%i != 0:
            prime = True
            i+=1
        else:
            prime = False
            break
    
    #check if k is prime
    if prime:
        print(k)
        all_primes.append(k)

    k+=1

#see the output in the form of an array
print(all_primes)