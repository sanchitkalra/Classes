
from sys import stdin


def pairSum(arr, n, x) :
    counter = 0
    for k in range(n):
        for j in range(k+1, n):
            if (arr[k] + arr[j] == x) and (k != j):
                counter += 1
                continue
    
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
    print(pairSum(arr, n, x))

    t -= 1


# logical testing

# arr = [1, 3, 6, 2, 5, 4, 3, 2, 4]
# arr = [1, 3, 6, 2, 5, 4, 3, 2, 4]
# #arr = [2, 8, 10, 5, -2, 5]

# sum = 7
# counter = 0

# for k in range(len(arr)):
#     for j in range(k+1, len(arr)):
#         if (arr[k] + arr[j] == sum) and (k!=j):
#             print("pair is k: {} and j: {}".format(arr[k], arr[j]))
#             counter += 1
#             continue
# print(counter)