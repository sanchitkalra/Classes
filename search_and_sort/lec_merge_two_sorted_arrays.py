from sys import stdin

def merge(arr1, n, arr2, m) : 
    i = 0
    j = 0
    merge = []
    while i < n and j < m:
        if arr1[i] > arr2[j]:
            merge.append(arr2[j])
            j += 1
        else:
            merge.append(arr1[i])
            i += 1
    while i < n:
        merge.append(arr1[i])
        i += 1
    while j < m:
        merge.append(arr2[j])
        j += 1
    return merge

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1

# ---------------
# logical testing
# ---------------

arr1 = [1, 4, 9, 10]
arr2 = [2, 3, 6, 7, 8]

merge = []

i = 0
j = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] > arr2[j]:
        merge.append(arr2[j])
        j += 1
    else:
        merge.append(arr1[i])
        i += 1
while i < len(arr1):
    merge.append(arr1[i])
    i += 1
while j < len(arr2):
    merge.append(arr2[j])
    j += 1

print(merge)