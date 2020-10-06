
from sys import stdin

def findTriplet(arr, n, x) :
    counter = 0
    for k in range(n):
        for j in range(k+1, n):
            for i in range(j+1, n):
                if arr[k] + arr[j] + arr[i] == x:
                    counter += 1
    return counter
    
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n



#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(findTriplet(arr, n, x))
    t -= 1

# logical testing

# arr = [1, 2, 3, 4, 5, 6, 7]

# counter = 0
# for k in range(len(arr)):
#     for j in range(k+1, len(arr)):
#         for i in range(j+1, len(arr)):
#             if (arr[k] + arr[j] + arr[i] == 12):
#                 counter  += 1

# print(counter)