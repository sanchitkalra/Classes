from sys import stdin

def spiralPrint(mat, nRows, mCols):
    #Your code goes here
    if not (nRows == 0 and mCols == 0):
        r_s = 0
        r_e = len(mat) - 1

        c_s = 0
        c_e = len(mat[0]) - 1

        while r_s <= r_e:
            for k in range(c_s, c_e+1):
                print(mat[r_s][k], end = " ")
            for k in range(r_s+1, r_e+1):
                print(mat[k][c_e], end = " ")
            for k in range(c_e-1, c_s-1, -1):
                print(mat[r_e][k], end = " ")
            for k in range(r_e-1, r_s, -1):
                print(mat[k][c_s], end = " ")
            r_s += 1
            c_s += 1
            r_e -= 1
            c_e -= 1

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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1

# ---------------
# logical testing
# ---------------

# arr = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

r_s = 0
r_e = len(arr) - 1

c_s = 0
c_e = len(arr[0]) - 1

while r_s <= r_e:
    for k in range(c_s, c_e+1):
        print(arr[r_s][k], end = " ")
    for k in range(r_s+1, r_e+1):
        print(arr[k][c_e], end = " ")
    for k in range(c_e-1, c_s-1, -1):
        print(arr[r_e][k], end = " ")
    for k in range(r_e-1, r_s, -1):
        print(arr[k][c_s], end = " ")
    r_s += 1
    c_s += 1
    r_e -= 1
    c_e -= 1

# while r_s <= r_e:
#     for k in range(c_s, c_e+1):
#         print(arr[r_s][k], end = " ")
#     c_s += 1
#     for k in range(r_s+1, r_e+1):
#         print(arr[k][c_e], end = " ")
#     c_e -= 1
#     for k in range(c_s, c_e):
#         print(arr[r_e][k], end = " ")
#     r_e -= 1
#     for k in range(r_s+1, r_e):
#         print(arr[k][c_s-1], end = " ")
#     r_s += 1