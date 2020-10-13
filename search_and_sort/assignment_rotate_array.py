from sys import stdin


def rotate(arr, n, d):
    result = []

    for k in range(d, len(arr)):
        result.append(arr[k])
    for k in range(d):
        result.append(arr[k])
    for k in range(len(result)):
        arr[k] = result[k]

# alternative solution
# def rotate(arr, n, d):
#     for i in range(d):
#         temp = arr[0]
#         for k in range(1, len(arr)):
#             arr[k], arr[k-1] = arr[k-1], arr[k]

#         arr[len(arr)-1] = temp

# alternative solution
# def rotate(arr, n, d):
#     temp = []
#     for k in range(d):
#         temp.append(arr[k])
#     for k in range(d, len(arr)):
#         arr[k], arr[k-d] = arr[k-d], arr[k]
#     for k in range(d):
#         arr[len(arr)-d+k] = temp[k]

#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1

# ---------------
# logical testing
# ---------------

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
result = []

for k in range(d, len(arr)):
    result.append(arr[k])
for k in range(d):
    result.append(arr[k])
for k in range(len(result)):
    arr[k] = result[k]

print(arr)

arr = [1, 2, 3, 4, 5, 6, 7]

for i in range(d):
    temp = arr[0]
    for k in range(1, len(arr)):
        arr[k], arr[k-1] = arr[k-1], arr[k]

    arr[len(arr)-1] = temp

print(arr)

arr = [1, 2, 3, 4, 5, 6, 7]
rotate(arr, 1, 2)
print(arr)
