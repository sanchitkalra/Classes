from sys import stdin


def secondLargestElement(arr, n):
    #Your code goes here
    largest = 0
    for k in arr:
        if k >= largest:
            largest = k
    count = arr.count(largest)
    for k in range(count):
        arr.remove(largest)
    largest = 0
    if len(arr) == 0:
        largest = -2147483648
    else:
        for k in arr:
            if k >= largest:
                largest = k
    return largest

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0



#main
t = int(stdin.readline().rstrip())

while t > 0 : 
    
    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1

# ---------------
# logical testing
# ---------------

arr = [2, 13, 4, 1, 3, 6, 28]
#arr = [9, 3, 6, 2, 9]
arr = [90, 8, 90, 5]
largest = 0

# for k in arr:
#     if k >= second and k >= largest:
#         second = largest
#         largest = k
#     elif k >= second and k < largest:
#         second = k
#     print("largest is ", largest)
#     print("second is ", second)

for k in arr:
    if k >= largest:
        largest = k

count = arr.count(largest)

for k in range(count):
    arr.remove(largest)

largest = 0

if len(arr) == 0:
    print(-2147483648)
else:
    for k in arr:
        if k >= largest:
            largest = k

print(largest)
