from sys import stdin

def arrayRotateCheck(arr, n):
    index = 0

    for k in range(len(arr)-1):
        if arr[k+1] < arr[k]:
            index = k + 1

    return index

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(arrayRotateCheck(arr, n))

    t -= 1

# ---------------
# logical testing
# ---------------

arr = [10, 20, 30, 1]

index = 0

for k in range(len(arr)-1):
    if arr[k+1] < arr[k]:
        index = k + 1

print(index)