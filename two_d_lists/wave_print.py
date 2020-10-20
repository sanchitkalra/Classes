from sys import stdin

def wavePrint(mat, nRows, mCols):
    #Your code goes here
    if not (nRows == 0 and mCols == 0):
        arr_print = []

        for k in range(len(mat[0])):
            temp = []
            for row in mat:
                temp.append(row[k])
            if k%2==0:
                arr_print.extend(temp)
            else:
                arr_print.extend(temp[::-1])

        for j in arr_print:
            print(j, end = " ")
    
#Taking Iput Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1

# ---------------
# logical testing
# ---------------

# print an array in a sine wave fashion

arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

arr_print = []

for k in range(len(arr[0])):
    temp = []
    for row in arr:
        temp.append(row[k])
    if k%2==0:
        arr_print.extend(temp)
    else:
        arr_print.extend(temp[::-1])

print(arr_print)