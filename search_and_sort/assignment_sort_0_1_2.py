from sys import stdin 

def sort012(arr, n) :
    zeros = 0
    ones = 0
    twos = 0

    for k in arr:
        if k == 0:
            zeros += 1
        elif k == 1:
            ones += 1
        else:
            twos += 1

    result = []

    for k in range(zeros):
        result.append(0)
    for k in range(ones):
        result.append(1)
    for k in range(twos):
        result.append(2)

    for k in range(len(result)):
        arr[k] = result[k]

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
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

    sort012(arr, n)
    printList(arr, n)
    
    t -= 1

# ---------------
# logical testing
# ---------------

arr = [0, 1, 2, 0, 2, 0, 1]

zeros = 0
ones = 0
twos = 0

for k in arr:
    if k == 0:
        zeros += 1
    elif k == 1:
        ones += 1
    else:
        twos += 1

result = []

for k in range(zeros):
    result.append(0)
for k in range(ones):
    result.append(1)
for k in range(twos):
    result.append(2)

for k in range(len(result)):
    arr[k] = result[k]

print(arr)