from sys import stdin

def bubbleSort(arr, n) :
    for i in range(len(arr)-1):
        for k in range(len(arr)-1-i):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
                
                
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
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
    bubbleSort(arr, n)
    printList(arr, n)

    t-= 1

# ---------------
# logical testing
# ---------------

arr = [6, 4, 8, 8, 1, 2, 2, 2, 4, 5, 6 ,7, 1, 1]

counter = 0

for i in range(len(arr)-1):
    for k in range(len(arr)-i-1):
        if arr[k] > arr[k+1]:
            arr[k], arr[k+1] = arr[k+1], arr[k]
            counter += 1
            print("arr at {}th itr is {}".format(counter, arr))
            continue
        counter += 1
        print("arr at {}th itr is {}".format(counter, arr))

print(arr)