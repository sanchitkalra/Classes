size = [int(x) for x in input().split()]

rows = size[0]
columns = size[1]

matrix = [ [ int(x) for x in input().split() ] for y in range(rows) ]

for row in matrix:
    row.reverse()

for row in matrix:
    for k in row:
        print(k, end = " ")
    print("")