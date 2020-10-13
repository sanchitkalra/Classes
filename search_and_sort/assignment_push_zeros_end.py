from sys import stdin

def pushZerosAtEnd(arr, n) :
    zeros = 0
    result = []
    for k in arr:
        if k == 0:
            zeros += 1
        else:
            result.append(k)
    for k in range(zeros):
        result.append(0)
    for k in range(len(result)):
        arr[k] = result[k]
    return arr

# alternative solution
# def pushZerosAtEnd(arr, n) :
#     i = 0
#     j = 0
#     for k in range(len(arr)):
#         if arr[k] != 0:
#             arr[i], arr[j] = arr[j], arr[i]
#             j += 1
#         i += 1
#     return arr
    
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split()))
    return arr, n
  

#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()

    pushZerosAtEnd(arr, n)
    printList(arr, n)

    t -= 1

# ---------------
# logical testing
# ---------------

arr = [2, 0, 0, 1, 3, 0, 0]

zeros = 0
result = []

for k in arr:
    if k == 0:
        zeros += 1
    else:
        result.append(k)
print(zeros)
for k in range(zeros):
    result.append(0)
print(result)

i = 0
j = 0

arr = [2, 0, 0, 1, 3, 0, 0]

for k in range(len(arr)):
    if arr[k] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1
    i += 1

print(arr)