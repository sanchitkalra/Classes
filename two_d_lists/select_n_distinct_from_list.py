size = int(input())
n_dist = int(input())

arr = [ int(x) for x in input().split() ]
combinations = []

for k in range(size):
    for j in range(k, size):
        pair = (arr[k], arr[j])
        pair_r = (arr[j], arr[k])
        if (pair not in combinations) and (pair_r not in combinations) and (arr[k] != arr[j]):
            combinations.append(pair)

print(combinations)