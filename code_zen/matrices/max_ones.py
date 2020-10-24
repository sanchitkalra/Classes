size = [int(x) for x in input().split()]

rows = size[0]
columns = size[1]

matrix = [ [ int(x) for x in input().split() ] for y in range(rows) ]

ones = {}

for index in range(len(matrix)):
    count = 0
    for k in matrix[index]:
        if k == 1:
            count += 1
    ones[index] = count

max_index = -1
max_count = -1
for key, value in ones.items():
    if value > max_count:
        max_count = value
        max_index = key
    
print(max_index)