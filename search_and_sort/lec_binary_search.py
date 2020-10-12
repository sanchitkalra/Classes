
from sys import stdin


def binarySearch(arr, n, x) :
    #Your code goes here
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    else:
        return -1
    
    
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
arr, n = takeInput()
t = int(stdin.readline().strip())

while t > 0 :
    
    x = int(input().strip())    
    print(binarySearch(arr, n, x))

    t -= 1

# ---------------
# logical testing
# ---------------

arr = [1, 3, 7, 9, 11, 12, 45]

start = 0
end = len(arr) - 1

x = 3

while start <= end:
    mid = (start+end)//2
    if arr[mid] == x:
        print(mid)
        break
    elif (arr[mid] > x):
        end = mid - 1
    else:
        start = mid + 1

else:
    print("-1")

# s 6
# e 6
# m 6