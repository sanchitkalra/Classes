'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))

'''

from sys import stdin

def max_row(arr):
    rows = len(arr)
    sum_arr = []
    for k in range(rows):
        sum_n = 0
        for element in arr[k]:
            sum_n += element
        sum_arr.append(sum_n)
    max_sum = max(sum_arr)
    max_sum_index = sum_arr.index(max_sum)
    return max_sum, max_sum_index

def max_column(arr):
    columns = len(arr[0])
    sum_arr = []
    for k in range(columns):
        sum_n = 0
        for row in arr:
            sum_n += row[k]
        sum_arr.append(sum_n)
    max_sum = max(sum_arr)
    max_sum_index = sum_arr.index(max_sum)
    return max_sum, max_sum_index

def compareForMax(row, column):
    row_m, row_m_index = row[0], row[1]
    column_m, column_m_index = column[0], column[1]
    if row_m >= column_m:
        print("row {} {}".format(row_m_index, row_m))
    else:
        print("column {} {}".format(column_m_index, column_m))

def findLargest(arr, nRows, mCols):
    #Your code goes here
    if nRows == 0 and mCols == 0:
        print("row 0 -2147483648")
    else:
        compareForMax(max_row(arr), max_column(arr))

#Taking Input Using Fast I/O
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
    findLargest(mat, nRows, mCols)

    t -= 1

# ---------------
# logical testing
# ---------------

# arr = [
#     [1, 2],
#     [90, 100],
#     [3, 40],
#     [-10, 200]
# ]

# arr = [
#     [3, 6, 9],
#     [1, 4, 7],
#     [2, 8, 9]
# ]

arr = [
    [1, 1],
    [1, 1]
]

# print(max_row(arr))
# print(max_column(arr))

compareForMax(max_row(arr), max_column(arr))