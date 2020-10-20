# method 1
# this function can also take input for jagged lists
# take input for each row in separate lines
def takeInputM1():
    size = [int(x) for x in input().split()]
    rows = size[0]

    matrix = [ [ int(x) for x in input().split() ] for x in range(rows) ]

    return matrix

#print(takeInputM1())

# method 2
# take input for all elements in one single input
def takeInputM2():
    size = [ int(x) for x in input().split() ]
    rows, columns = size[0], size[1]
    
    elements = [ int(x) for x in input().split() ]

    matrix = [ [ elements[columns*i + j] for j in range(columns) ] for i in range(rows) ]

    return matrix

#print(takeInputM2())