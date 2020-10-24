size = [int(x) for x in input().split()]

rows = size[0]
columns = size[1]

matrix = [ [ int(x) for x in input().split() ] for y in range(rows) ]

for row in matrix:
    for k in range(len(row)):
        sum = 0
        for j in range(k+1, len(row)):
            sum += row[j]
        row[k] = sum

for row in matrix:
    for k in row:
        print(k, end = " ")
    print("")