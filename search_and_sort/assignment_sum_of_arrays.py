from sys import stdin

def sumOfTwoArrays(arr1, n, arr2, m, output) :
    if len(arr1) == 0 and len(arr2) == 0:
        return [0]
    else:
        diff = abs(len(arr1) - len(arr2))

        if len(arr1) > len(arr2):
            for k in range(diff):
                arr2.insert(0, 0)
        elif len(arr2) > len(arr1):
            for k in range(diff):
                arr1.insert(0, 0)

        i = len(arr1)-1
        j = len(arr2)-1

        carry = 0
        result = []

        while i >= 0 and j >= 0:
            sum = arr1[i] + arr2[j] + carry
            if i != 0 and j != 0:
                x = sum % 10 # 0 
                y = int(sum/10) # 1 0
                result.append(x) # [0, 8]
                carry = y # 1 0
            else:
                result.append(sum) # [0, 8, 13]
            i -= 1
            j -= 1

        #result.reverse() # [13, 8, 0]
        #print(result)
        if result[len(result)-1] >= 10:
            x = result[len(result)-1]
            result[len(result)-1] = x // 10
            result.append(x%10)
            result[len(result)-1], result[len(result)-2] = result[len(result)-2], result[len(result)-1]
        
        for k in range(len(result)):
            output[k] = result[k]
        output.reverse()

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
    arr1, n = takeInput()
    arr2, m = takeInput()
    
    outputSize = (1 + max(n, m))
    output = outputSize * [0]
    
    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)
    
    t -= 1

# ---------------
# logical testing
# ---------------

arr1 = [6, 2, 4]
arr2 = [7, 5, 6]

arr1 = [8, 5, 2]
arr2 = [1, 3]

# arr1 = [9, 7, 6, 1]
# arr2 = [4, 5, 9]

diff = abs(len(arr1) - len(arr2))

if len(arr1) > len(arr2):
    for k in range(diff):
        arr2.insert(0, 0)
elif len(arr2) > len(arr1):
    for k in range(diff):
        arr1.insert(0, 0)

print("arr's after alteration are arr1: {} and arr2: {}".format(arr1, arr2))

i = len(arr1)-1
j = len(arr2)-1

carry = 0
result = []

while i >= 0 and j >= 0:
    sum = arr1[i] + arr2[j] + carry
    if i != 0 and j != 0:
        x = sum % 10 # 0 
        y = int(sum/10) # 1 0
        result.append(x) # [0, 8]
        carry = y # 1 0
    else:
        result.append(sum) # [0, 8, 13]
    i -= 1
    j -= 1
    print(result)

result.reverse() # [13, 8, 0]

print(result)