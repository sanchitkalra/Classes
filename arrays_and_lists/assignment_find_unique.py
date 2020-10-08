# this is the submitted solution, a better solution with the use of built in functions and a test logic is provided below

import sys

def findUnique(arr, n) :
    temp = []
    exp = 0
    for k in arr:
        for j in arr:
            if k == j:
                temp.append(k)
                continue
            else:
                exp = k
    length = len(temp)
    if length == 1:
        exp = arr[0]
    else:
        for k in range(0, length, 2):
            if k == (length-1):
                if temp[k] != temp[k-1]:
                    exp = temp[k]
                    break
            else:
                if temp[k] != temp[k+1]:
                    exp = temp[k]
                    break
    return exp

#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1

#---------------------------------------------------
# alternative solution using the count() function
# the following is a far better and optimal solution that you should use, the submitted solution achieves the same result without the use of any inbuilt functions
#---------------------------------------------------

arr = [
    [2, 3, 1, 6, 3, 6, 2],
    [2, 4, 7, 2, 7],
    [1, 3, 1, 3, 6, 6, 7, 10, 7],
    [2, 3, 6, 3, 6, 2, 1],
]

for i in range(4):
    print("current case ", i)
    ar = arr[i]
    exp = 0
    print("current arr: ", ar)
    for k in range(len(ar)):
        if ar.count(ar[k]) == 1:
            exp = ar[k]
            break
    print("exp is " + str(exp))
    print("-------------------")

#---------------------------------------------------
# alternative solution without the use of any in-built function
#---------------------------------------------------

for i in range(n):
        for j in range(n):
            if (i != j) and (arr[i] == arr[j]):
                break
        else:
            print(arr[i])

#---------------------------------------------------
#test logic
#---------------------------------------------------

arr = [
    [2, 3, 1, 6, 3, 6, 2],
    [2, 4, 7, 2, 7],
    [1, 3, 1, 3, 6, 6, 7, 10, 7],
    [2, 3, 6, 3, 6, 2, 1],
]

for i in range(4):
    print("current case ", i)
    ar = arr[i]
    print("current arr: ", ar)
    temp = []
    exp = 0
    for k in ar:
        for j in ar:
            if k == j:
                temp.append(k)
                continue
            else:
                exp = k
    length = len(temp)
    if length == 1:
        exp = arr[0]
    else:
        for k in range(0, length, 2):
            if k == (length-1):
                if temp[k] != temp[k-1]:
                    exp = temp[k]
                    break
            else:
                if temp[k] != temp[k+1]:
                    exp = temp[k]
                    break
    print("exp is: ", exp)
    print("temp arr is: ", temp)
    print("---------------------")
    print("")